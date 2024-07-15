# MongoDB Scripts for NoSQL Operations

This repository contains Python and MongoDB scripts to perform various operations on a MongoDB database using pymongo.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x
- pymongo
- MongoDB 3.6 or higher

You can install pymongo using pip:

```bash
pip install pymongo

0-list_databases
This script lists all databases available on the MongoDB server.

1-use_or_create_database
This script switches to the specified database (my_db) or creates it if it doesn't exist.

2-insert
This script inserts a document into the collection "school" with the name "Holberton school".

3-all
This script lists all documents in the "school" collection.

4-match
This script lists all documents with name="Holberton school" in the "school" collection.

5-count
This script displays the number of documents in the "school" collection.

6-update
This script adds the attribute "address" with the value "972 Mission street" to all documents with name="Holberton school" in the "school" collection.

7-delete
This script deletes all documents with name="Holberton school" in the "school" collection.

8-all.py
This Python script defines a function list_all that lists all documents in a specified MongoDB collection using pymongo.
