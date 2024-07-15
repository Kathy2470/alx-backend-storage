#!/usr/bin/env python3
"""
11-schools_by_topic
"""
from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    """
    # Find documents where topics field contains the specified topic
    schools = list(mongo_collection.find({"topics": topic}))
    return schools

# For testing purposes
if __name__ == "__main__":
    # Example usage
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    # Sample data to insert into the collection
    j_schools = [
        { 'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
        { 'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        { 'name': "UCLA", 'topics': ["C", "Python"]},
        { 'name': "UCSD", 'topics': ["Cassandra"]},
        { 'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]
    
    # Insert sample data into the collection
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    # Query schools by topic "Python"
    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
