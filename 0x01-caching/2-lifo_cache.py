#!/usr/bin/env python3
"""
    LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFO Caching
    """
    def __init__(self):
        """
            Initialization
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
            Add cache data using the LIFO algorithm
        """
        if key is None or item is None:
            return
        if (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS and
            key not in self.cache_data
        ):
            discard_key = self.stack.pop()
            print(f"DISCARD: {discard_key}")
            del self.cache_data[discard_key]
        self.cache_data[key] = item
        self.stack.append(key)


my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()