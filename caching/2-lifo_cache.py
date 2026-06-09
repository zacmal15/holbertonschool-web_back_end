#!/usr/bin/env python3
"""This module defines a LIFO caching system."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class implements a cache using the LIFO procedure."""
    
    def __init__(self):
        """Initialises the cache and track insertion order."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache using the LIFO replacement proecdure."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.order.pop(-2)
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Return the value associated wit a key."""
        if key is None:
            return None

        return self.cache_data.get(key)
