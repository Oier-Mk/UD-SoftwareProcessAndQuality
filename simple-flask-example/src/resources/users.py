from flask import request
from flask_restful import Resource
from models import User

class Users(Resource):
    def get(self):
        users = []
        users.append(User(0, "John", "Smith"))
        return [user.__dict__ for user in users]
    
    def post(self):
        data = request.json
        print(f'Received new user: {data}')


class UsersDetail(Resource):
    def get(self, code):
        return '', 200
    
    def delete(self, code):
        if code == 10:
            print('Deleting user...')
            return '', 200
        else:
            return '', 404