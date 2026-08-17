#!/usr/bin/env python3
""" 11-main """

from pymongo import MongoClient


if __name__ == "__main__":
    """ connection to mongddb and check logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    count_logs = nginx_collection.estimated_document_count()
    print(f"{count_logs} logs")

    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for methods in method:
        count_methods = nginx_collection.count_documents({"method": methods})
        print(f"\tmethod {methods}: {count_methods}")

    sc = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{sc} status check")
