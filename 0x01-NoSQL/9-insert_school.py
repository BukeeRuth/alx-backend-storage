#!/usr/bin/env python3
""" inserts a  ew document """

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.
    kwargs: Key-value pairs to be inserted as the new document.

    Returns:
    ObjectId: The _id of the newly inserted document.
    """
    if mongo_collection is None:
        return None

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
