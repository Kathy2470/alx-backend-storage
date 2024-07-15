#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def count_logs(mongo_collection):
    """
    Counts total number of logs in collection
    """
    total_logs = mongo_collection.count_documents({})
    return total_logs

def count_methods(mongo_collection):
    """
    Counts number of logs for each HTTP method
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    return method_counts

def count_status_check(mongo_collection):
    """
    Counts number of logs where method=GET and path=/status
    """
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    return status_check_count

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    
    total_logs = count_logs(collection)
    methods_counts = count_methods(collection)
    status_check_count = count_status_check(collection)
    
    # Output formatting
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
