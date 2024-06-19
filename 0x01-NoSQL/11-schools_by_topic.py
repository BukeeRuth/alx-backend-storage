#!/usr/bin/env python3
""" returns the list of school having a specific topic """

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.
    topic (str): The topic to search for.

    Returns:
    list: A list of dictionaries representing the schools with the specified topic.
    """
    if mongo_collection is None or not topic:
        return []

    return list(mongo_collection.find({"topics": topic}))
