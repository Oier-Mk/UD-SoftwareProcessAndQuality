from flask_restful import Resource

# Simple resource that returns the message 'Got it!' when it receives a GET request to its URL
class MyResource(Resource):
    def get(self):
        return "Got it!"