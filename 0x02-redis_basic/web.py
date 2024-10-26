#!/usr/bin/env python3
"""A module with tools for request caching and tracking."""


import redis
import requests
from functools import wraps
from typing import Callable


# Create a Redis instance to interact with the Redis database
redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Caches the output of fetched data."""
    @wraps(method)
    def invoker(url) -> str:
        """Wrapper function for caching the output."""
        # Increment the request count for the given URL in Redis
        redis_store.incr(f"count:{url}")

        # Check if there is a cached result for the given URL
        result = redis_store.get(f"result:{url}")
        if result:
            # Decode and return the cached result if it exists
            return result.decode("utf-8")

        # Fetch fresh data from the URL and cache it if no cached result exists
        result = method(url)

        # Initialize the request count for the URL in Redis if
        # it's newly cached
        redis_store.set(f"count:{url}", 0)

        # Cache the result with a 10-second expiration time
        redis_store.setex(f"result:{url}", 10, result)

        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Fetches the content of a URL and caches the response."""
    return requests.get(url).text
