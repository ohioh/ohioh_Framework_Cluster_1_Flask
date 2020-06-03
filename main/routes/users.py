import json
from flask import request
from main import mongo
from flask_restful import Resource
from ..schemas.users import UserSchema
from ..services.db import DbOperations
from bson.objectid import ObjectId


users = mongo.ohioh.users
db = DbOperations(collections=users, schema=UserSchema)


class UserList(Resource):
    def get(self):
        return db.find_all()

    def post(self):
        payload = request.get_json()
        return db.insert(payload)


class User(Resource):
    def get(self, user_id):
        return db.find_one(
            criteria={'_id': ObjectId(user_id)}
        )

    def put(self, user_id):
        payload = request.get_json()
        return db.update(
            criteria={'_id': ObjectId(user_id)},
            updated_value=payload
        )

    def delete(self, user_id):
        return db.delete(
            criteria={'_id': ObjectId(user_id)}
        )
