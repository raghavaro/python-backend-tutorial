from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    
    def get(self):
        return {'method': 'GET', 'data': 'hello world'}

    def post(self):
        return {'method': 'POST', 'data': 'hello world'}

    def patch(self):
        return {'method': 'PATCH', 'data': 'hello world'}

    def delete(self):
        return {'method': 'DELETE', 'data': 'hello world'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
