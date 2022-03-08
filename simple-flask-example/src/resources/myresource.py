from flask_restful import Resource

class MyResource(Resource):
    def get(self):
        return "Got it!"