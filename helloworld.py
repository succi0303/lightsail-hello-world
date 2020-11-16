from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Greeting(Resource):
    def get(self):
        return {"message": "Hello Flask API World!"}


api.add_resource(Greeting, '/')

if __name__ == '__main__':
    app.run('0.0.0.0', '8080')
