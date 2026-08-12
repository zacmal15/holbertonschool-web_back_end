#!/usr/bin/env python3
"""Module for finding schools by topic in Monogdb."""


def schools_by_topic(mongo_collection, topic):
    """Return all schools that contain specified topic."""
    return mongo_collection.find({"topics": topic})
