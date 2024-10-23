#!/usr/bin/env python3
"""
Exercise module for Redis Cache
"""

import redis
import uuid
from typing import Callable, Union
import functools


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the call count for the method and call the original method."""
        # Increment the count in Redis using the method's qualified name as the key
        self._redis.incr(method.__qualname__)
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis connection and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls  # Apply the count_calls decorator to store method
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
    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))  # Should print b'1'

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))  # Should print b'3'

