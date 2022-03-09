from flask import request
from flask_restful import Resource
from models import User

# This resource is related to the URL '/users'. It refers to all users saved in the server
# It performs an action when receiving either a GET or POST http request.
class Users(Resource):
    # GET http method: get all users in the server.
    def get(self):
        users = []
        users.append(User(0, "John", "Smith"))
        return [user.__dict__ for user in users]
    
    # POST http method: create a new user in the server.
    def post(self):
        data = request.json
        print(f'Received new user: {data}')


# This resource is related to the URL '/users/<int:code>'. It refers to a single user saved in the server.
# It performs an action when receiving either a GET or DELETE http request.
class UsersDetail(Resource):
    # GET http method: get a single user in the server.
    def get(self, code):
        return '', 200
    
    # DELETE http method: delete a single user in the server.
    def delete(self, code):
        if code == 10:
            print('Deleting user...')
            return '', 200
        else:
            return '', 404