#!/usr/bin/env python3
"""
    FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Add cache data using the FIFO algorithm
        """
        if key is None or item is None:
            return
        else:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data
            ):
                for k, v in self.cache_data.items():
                    discard_key = k
                    discard_item = v
                    break
                print(f"DISCARD: {discard_key}")
                del self.cache_data[discard_key]
            self.cache_data[key] = item

    def get(self, key):
        """
            Return the value in self.cache_data linked to key.
        """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
