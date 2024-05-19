#!/usr/bin/python3
"""Define the data models for the quiz application"""
from bson import ObjectId

class Quiz:
    def __init__(self, title, description, questions, author):
        self.title = title
        self.description = description
        self.questions = questions
        self.author = author

    def to_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "questions": self.questions,
            "author": self.author
        }

class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

    def to_json(self):
        retutn {
            "question_text": self.question_text,
            "options": self.optpions,
            "correct_option": self.correct_option
        }
