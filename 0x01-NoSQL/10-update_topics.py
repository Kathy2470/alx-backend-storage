#!/usr/bin/env python3
"""
10-update_topics
"""
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    """
    # Update the document where name matches
    result = mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
    return result.modified_count

# For testing purposes
if __name__ == "__main__":
    # Example usage
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    
    # Update topics for "Holberton school" initially
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    # Print all schools after the first update
    schools = list(school_collection.find())
    for school in schools:
        topics = school.get('topics', [])
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), topics))

    # Update topics again for "Holberton school"
    update_topics(school_collection, "Holberton school", ["iOS"])

    # Print all schools after the second update
    schools = list(school_collection.find())
    for school in schools:
        topics = school.get('topics', [])
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), topics))
