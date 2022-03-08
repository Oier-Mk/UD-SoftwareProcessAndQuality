from flask import Flask
from flask_restful import Api
from resources import MyResource, Users, UsersDetail
import os

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET')
api = Api(app)


api.add_resource(MyResource, '/myresource')
api.add_resource(Users, '/users')
api.add_resource(UsersDetail, '/users/<int:code>')


if __name__ == '__main__':
    app.run(debug=True)