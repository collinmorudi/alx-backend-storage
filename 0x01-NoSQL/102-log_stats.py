#!/usr/bin/env python3
"""Task 15's module."""


from pymongo import MongoClient


def display_log_statistics(nginx_collection):
    """Displays statistics about Nginx request logs."""

    total_logs = nginx_collection.count_documents({})
    print(f'{total_logs} logs')
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = nginx_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {method_count}')
    status_checks = nginx_collection.count_documents(
                    {'method': 'GET', 'path': '/status'})
    print(f'{status_checks} status check')


def display_top_ips(nginx_collection):
    """Displays the top 10 HTTP IPs in the collection."""
    print('IPs:')
    top_ips = nginx_collection.aggregate(
        [
            {'$group': {'_id': "$ip", 'requestCount': {'$sum': 1}}},
            {'$sort': {'requestCount': -1}},
            {'$limit': 10}
        ]
    )
    for ip_log in top_ips:
        ip = ip_log['_id']
        request_count = ip_log['requestCount']
        print(f'\t{ip}: {request_count}')


def main():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    display_log_statistics(client.logs.nginx)
    display_top_ips(client.logs.nginx)


if __name__ == '__main__':
    main()
