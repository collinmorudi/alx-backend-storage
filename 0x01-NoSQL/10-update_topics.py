#!/usr/bin/env python3
"""Module that updates the topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The name of the school to update.
        topics (list): A list of strings representing the topics.

    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
