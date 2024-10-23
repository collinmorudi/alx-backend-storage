#!/usr/bin/env python3
"""web"""


import redis
import requests
from typing import Callable
import functools


# Connect to Redis
redis_client = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """Decorator to cache a page and track URL access."""
    @functools.wraps(method)
    def wrapper(url: str) -> str:
        """Check if URL content is cached, otherwise fetch and cache."""
        # Create the Redis keys for count and caching
        count_key = f"count:{url}"
        cache_key = f"cached:{url}"

        # Increment the access count for this URL
        redis_client.incr(count_key)

        # Try to get the cached page content
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # If not cached, fetch the content from the URL
        content = method(url)

        # Cache the content with a 10-second expiration
        redis_client.setex(cache_key, 10, content)

        return content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL."""
    response = requests.get(url)
    return response.text


# Example usage:
if __name__ == "__main__":
    url = "http: // slowwly.robertomurray.co.uk/delay/3000/url/http://www.example.com"

    # First access: will fetch from the URL
    print(get_page(url))

    # Subsequent accesses within 10 seconds: will return cached content
    print(get_page(url))

    # Check how many times the URL was accessed
    print(f"URL was accessed {redis_client.get(f'count:{url}').decode('utf-8')} times.")
