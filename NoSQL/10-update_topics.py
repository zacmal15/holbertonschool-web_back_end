#!/usr/bin/env python3
"""Module for updating school topics in mongodb"""


def updatee_topics(mongo_collection, topics):
    """Update topics of all schools with matching names."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
