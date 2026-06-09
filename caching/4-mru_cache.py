#!/usr/bin/env python3
"""This module defines a MRU caching system."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This class implements a cache using the MRU replacement procedure."""

    def __init__(self):
        """Initialises the cache and track recently used keys."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache using the MRU replacement procedure."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.order.pop(-2)
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Return the value linked to the given key from the cache."""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data.get(key)
