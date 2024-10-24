#!/usr/bin/env python3
"""
Exercise module for Redis Cache
"""


import redis
import uuid
from typing import Callable, Union, Any
import functools


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method of Cache class is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Increments the call counter and then invokes the method.
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to track the call history (inputs and outputs) of a method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Stores method input arguments and output results in Redis.
        """
        in_key = f'{method.__qualname__}:inputs'
        out_key = f'{method.__qualname__}:outputs'

        # Store input arguments
        self._redis.rpush(in_key, str(args))

        # Invoke the method and store its output
        output = method(self, *args, **kwargs)
        self._redis.rpush(out_key, output)

        return output
    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls for a method in Cache class.
    """
    redis_store = method.__self__._redis
    method_name = method.__qualname__
    in_key = f'{method_name}:inputs'
    out_key = f'{method_name}:outputs'

    # Retrieve number of times method was called
    call_count = int(redis_store.get(method_name) or 0)
    print(f'{method_name} was called {call_count} times:')

    # Fetch and display inputs and outputs
    inputs = redis_store.lrange(in_key, 0, -1)
    outputs = redis_store.lrange(out_key, 0, -1)

    for input_val, output_val in zip(inputs, outputs):
        print(f'{method_name}(*{input_val.decode("utf-8")}) -> {output_val}')


class Cache:
    """Represents a cache system using Redis for data storage.
    """
    def __init__(self) -> None:
        """Initializes the Redis connection and clears the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis and returns a unique key for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable
            = None) -> Union[str, bytes, int, float]:
        """Retrieves data from Redis and optionally applies a conversion
        function.
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """Retrieves a string value from Redis and decodes it to UTF-8.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from Redis.
        """
        return self.get(key, int)
