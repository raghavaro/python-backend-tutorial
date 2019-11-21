from flask_mongoengine import MongoEngine
from books_and_reviews import app

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


