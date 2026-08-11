#!/usr/bin/env python3
"""Module for inserting a school into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new doc and return its ID."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
