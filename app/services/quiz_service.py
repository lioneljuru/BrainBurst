from app import mongo
from app.models import Quiz

def create_quiz(data):
    quiz = Quiz(**data)
    mongo.db.quizzes.insert_one(quiz.to_json())
    return quiz

def get_all_quizzes():
    quizzes = mongo.db.quizzes.find()
    return [Quiz(**quiz).to_json() for quiz in quizzes]

def get_quiz_by_id(quiz_id):
    quiz = mongo.db.quizzes.find_one({"_id": ObjectId(quiz_id)})
    if quiz:
        return Quiz(**quiz).to_json()
    return None
