#!/usr/bin/env python3
""" 102-log_stats.py """


from pymongo import MongoClient
from collections import Counter


def print_log_stats():
    """todo: add comments"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count methods
    methods_count = nginx_collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ])
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = next((item['count'] for item in methods_count
                      if item['_id'] == method), 0)
        print(f"\tmethod {method}: {count}")

    # Count status check
    status_check_count = nginx_collection.count_documents(
                         {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # Top 10 IPs
    print("IPs:")
    ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    print_log_stats()
