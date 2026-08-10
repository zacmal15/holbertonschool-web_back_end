#!/usr/bin/python3
"""This module defines a basic caching system."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This class implements a basic caching system."""

    def put(self, key, item):
        """Store an item in the cache."""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None:
            return None

        return self.cache_data.get(key)
