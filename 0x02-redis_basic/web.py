#!/usr/bin/env python3
"""
Module web.py to fetch and cache web pages using Redis.
"""

import redis
import requests
from typing import Callable
from functools import wraps


def count_requests(method: Callable) -> Callable:
    """
    Decorator to count the number of requests made to a URL.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """
        Wrapper function to increment the request count.
        """
        url = args[0]
        redis_instance = redis.Redis()
        redis_instance.incr(f"count:{url}")
        return method(*args, **kwargs)
    return wrapper


def cache_page(method: Callable) -> Callable:
    """
    Decorator to cache the result of fetching a web page.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """
        Wrapper function to cache the page content.
        """
        url = args[0]
        redis_instance = redis.Redis()
        cached_content = redis_instance.get(f"cached:{url}")
        if cached_content:
            return cached_content.decode('utf-8')
        content = method(*args, **kwargs)
        redis_instance.setex(f"cached:{url}", 10, content)
        return content
    return wrapper


@count_requests
@cache_page
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a particular URL.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
