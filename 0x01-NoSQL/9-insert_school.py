#!/usr/bin/env python3
"""
9-insert_school
"""
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    # Insert the document and capture the inserted_id
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

# For testing purposes
if __name__ == "__main__":
    # Example usage
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    
    # Insert a new school document
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))
