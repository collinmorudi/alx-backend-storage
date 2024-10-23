#!/usr/bin/env python3
"""
Exercise module for Redis Cache
"""

import redis
import uuid
from typing import Callable, Union
import functools


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Store inputs and outputs in Redis and return the result."""
        # Generate Redis keys for storing inputs and outputs
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store the inputs (args) in the inputs list
        self._redis.rpush(input_key, str(args))

        # Call the original method and get the output
        output = method(self, *args, **kwargs)

        # Store the output in the outputs list
        self._redis.rpush(output_key, str(output))

        # Return the original output
        return output

    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis connection and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history  # Apply the call_history decorator to store method
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis using a randomly generated key and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and apply the conversion function if provided."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve a string from Redis."""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieve an integer from Redis."""
        return self.get(key, fn=int)


# Example usage:
if __name__ == "__main__":
    cache = Cache()

    # Store some values
    s1 = cache.store("first")
    print(s1)  # Should print the key for "first"

    s2 = cache.store("secont")
    print(s2)  # Should print the key for "secont"

    s3 = cache.store("third")
    print(s3)  # Should print the key for "third"

    # Retrieve the input and output history
    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    # Print the inputs and outputs history
    print(f"inputs: {inputs}")
    print(f"outputs: {outputs}")
