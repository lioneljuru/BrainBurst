#!/usr/bin/python3
"""
Business logic for handling operations
"""
from app import mongo
from app.models import Quiz

def create_quiz(data):
    """creates the quiz"""
    quiz = Quiz(**data)
    mongo.db.quizzes.insert_one(quiz.to_json())
    return quiz

def get_all_quizzes():
    """gets all the quizzes"""
    quizzes = mongo.db.quizzes.find()
    return [Quiz(**quiz).to_json() for quiz in quizzes]

def get_quiz_by_id(quiz_id):
    """uses id to access the quiz"""
    quiz = mongo.db.quizzes.find_one({"_id": ObjectId(quiz_id)})
    if quiz:
        return Quiz(**quiz).to_json()
    return None
