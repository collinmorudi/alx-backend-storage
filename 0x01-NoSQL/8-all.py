#!/usr/bin/env python3
"""Module that lists all documents in a MongoDB collection"""


def list_all(mongo_collection):
    """Lists all documents in a collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of all documents, or an empty list if no documents found.
    """
    return list(mongo_collection.find())
