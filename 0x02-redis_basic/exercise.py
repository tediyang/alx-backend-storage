#!/usr/bin/env python3
""" Setting up a class that writes to redis """
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """_summary_

        Args:
            data (str | float | bytes | int): the value to save

        Returns:
            str: the key returned.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """automatically parametrize Cache.get with the correct
        conversion function"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """automatically parametrize Cache.get with the correct
        conversion function"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
