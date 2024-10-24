#!/usr/bin/env python3
"""A module for handling web request caching and tracking access counts.
"""


import redis
import requests
from functools import wraps
from typing import Callable


cache_db = redis.Redis()
"""Redis instance for storing cache and tracking access.
"""


def cache_result(func: Callable) -> Callable:
    """Decorator that caches the output of a URL request.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """Checks cache before fetching the URL content and updates cache.
        """
        # Increment the access count for the URL
        cache_db.incr(f"count:{url}")

        # Check if result is already cached
        cached_result = cache_db.get(f"result:{url}")
        if cached_result:
            return cached_result.decode("utf-8")

        # If not cached, fetch and store the result with an expiration time
        response = func(url)
        cache_db.setex(f"result:{url}", 10, response)

        return response

    return wrapper


@cache_result
def get_page_content(url: str) -> str:
    """Fetches and returns the content of the given URL, caching the result.
    """
    return requests.get(url).text
