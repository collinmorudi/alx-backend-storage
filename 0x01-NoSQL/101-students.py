#!/usr/bin/env python3
"""101-students.py"""


from pymongo import MongoClient


def calculate_average_scores(students):
    """
    Calculate the average score for each student.

    Parameters:
    students (list): List of student documents.

    Returns:
    list: List of student documents with added 'averageScore' key.
    """
    for student in students:
        topics = student['topics']
        average_score = sum(topic['score'] for topic in topics) / len(topics)
        student['averageScore'] = average_score
    return students


def sort_students_by_average(students):
    """
    Sort students by their average score in descending order.

    Parameters:
    students (list): List of student documents.

    Returns:
    list: Sorted list of student documents.
    """
    return sorted(students, key=lambda x: x['averageScore'], reverse=True)


def top_students(mongo_collection):
    """
    Retrieve all students, calculate their average scores, and
    return them sorted by average score.

    Parameters:
    mongo_collection (MongoClient.collection): The MongoDB
    collection object.

    Returns:
    list: List of student documents sorted by 'averageScore' in
    descending order.
    """
    # Fetch all students from the collection
    students = list(mongo_collection.find())

    # Calculate average scores
    calculate_average_scores(students)

    # Sort students by average score
    sorted_students = sort_students_by_average(students)

    return sorted_students
