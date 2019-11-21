from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self):
        return { 'message': 'Books & Reviews API is running' }


class Books(Resource):
    def get(self):
        books = []
        # books = get all books
        return { 'message': 'Found books', 'data': books }

    def post(self):
        book = None
        # book = create a new book
        return { 'message': 'Created a new book', 'data': book }



class Book(Resource):
    def get(self, id):
        # get book by id
        return { 'message': 'Found a book', 'data': id }

    def patch(self, id):
        # get book by id and update it
        return { 'message': 'Updated the book', 'data': id }

    def delete(self, id):
        # get book by id and delete it
        return { 'message': 'Deleted the book', 'data': id }



api.add_resource(Index, '/')
api.add_resource(Books, '/books')
api.add_resource(Book, '/book/<id>')


if __name__ == '__main__':
    app.run(debug=True)
