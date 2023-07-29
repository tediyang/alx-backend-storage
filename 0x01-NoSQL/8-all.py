#!/usr/bin/python3
"""
    using pymongo collection to fetch all the data from the databse
"""


def list_all(mongo_collection):
    """
        this function uses a pymongo collection and returns the docs in the
        dabase
        Args:
            mongo_collection (_type_): the database collection

        Returns:
            List[Object]: returns a list of objects or NULL if none is present
    """
    return mongo_collection.find()
