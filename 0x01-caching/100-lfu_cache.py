#!/usr/bin/env python3
"""
    LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
        LFU Caching
    """
    def __init__(self):
        """
            Initialization
        """
        super().__init__()
        self.count = 0
        self.obj = {}

    def put(self, key, item):
        """
           Add cache data using the MRU algorithm
        """
        if key is None or item is None:
            return
        if (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS and
            key not in self.cache_data
        ):
            discard_key = None
            for k, v in self.obj.items():
                min = v
                discard_key = k
                break
            print(min)
            for k, v in self.obj.items():
                if v < min:
                    min = v
                    discard_key = k
            del self.cache_data[discard_key]
            del self.obj[discard_key]
            print(f"DISCARD: {discard_key}")
        self.cache_data[key] = item
        if key in self.obj:
            self.obj[key] += 1
        else:
            self.obj[key] = 1

    def get(self, key):
        """
            Return the value in self.cache_data linked to key.
        """
        if key in self.cache_data and key is not None:
            count = self.obj[key]
            del self.obj[key]
            self.obj[key] = count + 1
            return self.cache_data[key]
        else:
            return None
