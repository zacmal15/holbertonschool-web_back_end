#!/usr/bin/env python3
"""Provide some stats about Nginx logs stored in MongoDB.

This module connects to the MongoDB collection `logs.nginx` and
displays statistics about the documents it contains: the total
number of logs, the number of documents per HTTP method, and the
number of GET requests made to the `/status` path.
"""
from pymongo import MongoClient


def log_stats():
    """Display stats about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))


if __name__ == "__main__":
    log_stats()
