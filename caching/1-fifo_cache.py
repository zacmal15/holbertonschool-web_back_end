#!/usr/bin/env python3
"""This module defines a FIFO caching system."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This class implements a cache using the FIFO replacement procedure."""

    def __init__(self):
        """Initialises the FIFO cache and track insertion order."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache using the FIFO replacement proecudre."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.order.pop(0)
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

        def get(self, key):
            """Return the value linked to the given key from the cache."""
            if key is None:
                return None

            return self.cache_data.get(key)
