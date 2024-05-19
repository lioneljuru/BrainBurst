#!/usr/bin/python3
"""Contains the API end points"""
from flask import Blueprint, request, jsonify
from app.services import create_quiz, get_all_quizzes, 

bp = Blueprint('main', __name__)

@bp.route('/quizzes', methods=['GET'])
def fetch_quizzes():
    """gets all quizzes"""
    quizzes = get_all_quizzes()
    return jsonify(quizzes), 200

@bp.route('/quiz/<quizzes>', methods=['GET'])
def fetch_quiz(quiz_id):
    """gets the quiz by using id"""
    quiz = get_quiz_by_id(quiz_id)
    if quiz:
        return jsonify(quiz), 200
    return jsonify({"error": "Quiz not found"}), 404

@bp.route('/quizzes', methods=['POST'])
def add_quiz():
    """creates and adds a new quiz"""
    data = request.json
    quiz = create_quiz(data)
    return jsonify(quiz.to_json()), 201
