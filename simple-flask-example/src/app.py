from flask import Flask
from flask_restful import Api
from resources import MyResource, Users, UsersDetail
import os

# Main entry point of the application

app = Flask(__name__)   # Initialize the flask app
app.secret_key = os.environ.get('APP_SECRET')
api = Api(app)          # Initialize the flask_restful library


# Addition of resources. Those can be accesed throught a HTTP request to the path parameter (e.g. '/users')
api.add_resource(MyResource, '/myresource')
api.add_resource(Users, '/users')
api.add_resource(UsersDetail, '/users/<int:code>')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)