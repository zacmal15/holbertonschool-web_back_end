#!/usr/bin/env python3
"""Module for listing all docs in a MongoDB collection."""


def list_all(mongo_collection):
    """Return all docs from a MongoDB collection."""
    return list(mongo_collection.find())
