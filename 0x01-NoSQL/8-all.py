#!/usr/bin/env python3
""" function to list documents """

from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
    list: A list of all documents in the collection. Returns an empty list if no documents are found.
    """
    if mongo_collection is None:
        return []

    documents = list(mongo_collection.find())
    return documents