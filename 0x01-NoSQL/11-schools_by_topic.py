#!/usr/bin/env python3
"""
    a Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
        a function that fetches the documents with the provided topic

    Args:
        mongo_collection (_type_): collection connected to the database
        topic (str): name of topic
    """
    return mongo_collection.find({'topics': {'$elemMatch': {'$eq': topic}}})
