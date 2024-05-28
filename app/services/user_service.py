from app import mongo
from app.models import User

def create_user(data):
    user = User(**data)
    mongo.db.user.insert_one(user.to_json())
    return user

def get_all_user():
    users = mongo.db.users.find()
    return [User(**user).to_json() for user in users]

def get_user_by_id(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        return User(**user).to_json()
    return None
