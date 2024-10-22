#!/usr/bin/env python3
""" 102-log_stats """


from pymongo import MongoClient


def get_total_logs(nginx_collection):
    """
    Get the total number of logs.

    Parameters:
    nginx_collection (MongoClient.collection): The nginx collection object.
    
    Returns:
    int: Total number of logs.
    """
    return nginx_collection.count_documents({})


def get_method_distribution(nginx_collection):
    """
    Get the distribution of HTTP methods.

    Parameters:
    nginx_collection (MongoClient.collection): The nginx collection object.

    Returns:
    dict: Dictionary with HTTP methods as keys and their counts as values.
    """
    methods = {}
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        methods[method] = nginx_collection.count_documents({"method": method})
    return methods


def get_status_checks(nginx_collection):
    """
    Get the number of status checks.
    
    Parameters:
    nginx_collection (MongoClient.collection): The nginx collection object.
    
    Returns:
    int: Number of status checks.
    """
    return nginx_collection.count_documents({"method": "GET", "path": "/status"})


def get_top_ips(nginx_collection):
    """
    Get the top 10 most present IPs.
    
    Parameters:
    nginx_collection (MongoClient.collection): The nginx collection object.
    
    Returns:
    list: List of tuples containing IP addresses and their counts,
    sorted in descending order.
    """
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(nginx_collection.aggregate(pipeline))
    return [(ip["_id"], ip["count"]) for ip in top_ips]


def log_stats(mongo_collection):
    """
    Generate log statistics.

    Parameters:
    mongo_collection (MongoClient.collection): The nginx collection object.

    Returns:
    None
    """
    total_logs = get_total_logs(mongo_collection)
    method_distribution = get_method_distribution(mongo_collection)
    status_checks = get_status_checks(mongo_collection)
    top_ips = get_top_ips(mongo_collection)

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_distribution.items():
        print(f"    method {method}: {count}")
    print(f"{status_checks} status check")
    print("IPs:")
    for ip, count in top_ips:
        print(f"    {ip}: {count}")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
