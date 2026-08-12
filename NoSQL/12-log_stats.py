#!/usr/bin/env python3
"""Display statistics about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            nginx.count_documents({"method": method})
        ))

    print("{} status check".format(
        nginx.count_documents({"method": "GET", "path": "/status"})
    ))
