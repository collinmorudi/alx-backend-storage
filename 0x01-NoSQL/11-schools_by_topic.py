#!/usr/bin/env python3
"""Module to return schools with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of schools that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
