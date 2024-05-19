#!/usr/bin/python3
"""
This module initiates the Flask application
and the database connection.
"""
from flask import Flask
from app.config import Config
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    """Initiates the Flask application"""
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)

    with app.app_context():
        from app import routes

    return app
