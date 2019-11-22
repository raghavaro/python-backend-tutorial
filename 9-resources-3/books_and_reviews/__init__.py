from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/test'
}

from books_and_reviews.resources import *

api = Api(app)
api.add_resource(Index, '/')
api.add_resource(Books, '/books')
api.add_resource(Book, '/book/<id>')
api.add_resource(Reviews, '/book/<book_id>/reviews')
api.add_resource(Review, '/review/<id>')
