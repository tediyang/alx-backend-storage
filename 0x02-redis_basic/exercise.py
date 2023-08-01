#!/usr/bin/env python3
""" Setting up a class that writes to redis """
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """
        A class Cache that writes and stores value in Redis
    """
    def __init__(self):
        """
            setup the redis database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """_summary_

        Args:
            data (str | float | bytes | int): the value to save

        Returns:
            str: the key returned.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
