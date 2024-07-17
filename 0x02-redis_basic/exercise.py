#!/usr/bin/env python3
"""
This module provides the Cache class for storing data in Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class to interact with Redis.
    """

    def __init__(self):
        """
        Initializes the Cache instance with a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis and applies a conversion function if provided.

        Args:
            key (str): The key of the data to be retrieved.
            fn (Optional[Callable]): A function to convert the data to the desired format.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data from Redis and converts it to a UTF-8 string.

        Args:
            key (str): The key of the data to be retrieved.

        Returns:
            Optional[str]: The retrieved data as a UTF-8 string, or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data from Redis and converts it to an integer.

        Args:
            key (str): The key of the data to be retrieved.

        Returns:
            Optional[int]: The retrieved data as an integer, or None if the key does not exist.
        """
        return self.get(key, lambda d: int(d))
