#!/usr/bin/env python3
"""Script to analyze Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def main():
    """ Connect to MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs  # Database name
    nginx_collection = db.nginx  # Collection name

    # Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count specific request
    status_check_count = nginx_collection.count_documents(
                         {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    main()
