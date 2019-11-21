from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/test'
}
db = MongoEngine()
db.init_app(app)


class Book(db.Document):
    title = db.StringField(required=True)
    author = db.StringField(required=True)
    isbn = db.StringField(unique=True)


class Review(db.Document):
    recommend = db.BooleanField(default=False)
    text = db.StringField()
    book = db.ReferenceField('Book')


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



class Reviews(Resource):
    def get(self, book_id):
        reviews = []
        # reviews = get all reviews for book with id = book_id
        return { 'message': 'Found reviews for book {}'.format(book_id), 'data': reviews }

    def post(self, book_id):
        review = None
        # review = create a new review for book with id = book_id
        return { 'message': 'Created a new review', 'data': review }


class Review(Resource):
    def get(self, id):
        # get review by id
        return { 'message': 'Found a review', 'data': id }

    def patch(self, id):
        # get review by id and update it
        return { 'message': 'Updated the review', 'data': id }

    def delete(self, id):
        # get review by id and delete it
        return { 'message': 'Deleted the review', 'data': id }

api.add_resource(Index, '/')
api.add_resource(Books, '/books')
api.add_resource(Book, '/book/<id>')
api.add_resource(Reviews, '/book/<book_id>/reviews')
api.add_resource(Review, '/review/<id>')

if __name__ == '__main__':
    app.run(debug=True)
