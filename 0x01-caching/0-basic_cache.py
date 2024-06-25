#!/usr/bin/env python3
"""
    Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        """
            Initialization
        """
        super().__init__()
    def put(self, key, item):
        """
            Must assign to the dictionary self.cache_data the
            item value for the key 'key'
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key.
        """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
