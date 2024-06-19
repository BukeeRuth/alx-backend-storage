#!/usr/bin/env python3
""" updates topics of a document """

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.
    name (str): The name of the school to update.
    topics (list of str): The list of topics approached in the school.

    Returns:
    None
    """
    if mongo_collection is None or not name or not topics:
        return None

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
