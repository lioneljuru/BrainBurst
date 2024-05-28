import pytest
from app import create_app
from flask import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_fetch_quizzes(client):
    response = client.get('/quizzes')
    assert response.status_code == 200

def test_add_quiz(client):
    new_quiz = {
        "title": "Sample Quiz",
        "description": "This is a sample",
        "questions": [],
        "author": "Author"
    }
    response = client.post('/quizzes', data=json.dumps(new_quiz), content_type='application/json')
    assert response.status_code == 201
