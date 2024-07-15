#!/usr/bin/env python3
"""
List all documents in a collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection to list documents from.

    Returns:
        list: A list of documents, or an empty list if no documents are found.
    """
    return list(mongo_collection.find())

