#!/usr/bin/env python3
"""
    MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
        MRU Caching
    """
    def __init__(self):
        """
            Initialization
        """
        super().__init__()
        self.stack = [k for k, v in self.cache_data.items()]

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
            if self.stack and len(self.stack) > 1:
                discard_key = self.stack[-1]
                self.stack.pop(-1)
            else:
                for k, v in self.cache_data.items():
                    discard_key = k
                    break

            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")
        if key in self.stack:
            self.stack.pop(self.stack.index(key))
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """
            Return the value in self.cache_data linked to key.
        """
        if key in self.cache_data and key is not None:
            self.stack.pop(self.stack.index(key))
            self.stack.append(key)
            return self.cache_data[key]
        else:
            return None
