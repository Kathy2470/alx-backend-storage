#!/usr/bin/env python3
"""
Function top_students:
Returns all students sorted by average score.

Args:
- mongo_collection: pymongo collection object representing the 'students' collection.

Returns:
- List of dictionaries, each representing a student with an added key 'averageScore'.
"""

def top_students(mongo_collection):
    pipeline = [
        { "$unwind": "$topics" },
        { "$group": {
            "_id": "$_id",
            "name": { "$first": "$name" },
            "averageScore": { "$avg": "$topics.score" }
        }},
        { "$sort": { "averageScore": -1 } }
    ]

    students = list(mongo_collection.aggregate(pipeline))
    for student in students:
        student['_id'] = str(student['_id'])  # Convert ObjectId to string for printing or further processing

    return students

# For testing purposes
if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students

    # Example data insertion (assuming you have a function insert_school that inserts data)
    j_students = [
        { 'name': "John", 'topics': [{ 'title': "Algo", 'score': 10.3 },{ 'title': "C", 'score': 6.2 }, { 'title': "Python", 'score': 12.1 }]},
        { 'name': "Bob", 'topics': [{ 'title': "Algo", 'score': 5.4 },{ 'title': "C", 'score': 4.9 }, { 'title': "Python", 'score': 7.9 }]},
        { 'name': "Sonia", 'topics': [{ 'title': "Algo", 'score': 14.8 },{ 'title': "C", 'score': 8.8 }, { 'title': "Python", 'score': 15.7 }]},
        { 'name': "Amy", 'topics': [{ 'title': "Algo", 'score': 9.1 },{ 'title': "C", 'score': 14.2 }, { 'title': "Python", 'score': 4.8 }]},
        { 'name': "Julia", 'topics': [{ 'title': "Algo", 'score': 10.5 },{ 'title': "C", 'score': 10.2 }, { 'title': "Python", 'score': 10.1 }]}
    ]

    for j_student in j_students:
        insert_school(students_collection, **j_student)

    # Retrieve and print top students
    top_students_list = top_students(students_collection)
    for student in top_students_list:
        print("[{}] {} => {}".format(student.get('_id'), student.get('name'), student.get('averageScore')))
