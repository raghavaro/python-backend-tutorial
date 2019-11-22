from flask_mongoengine import MongoEngine
from books_and_reviews import app

db = MongoEngine()
db.init_app(app)


class Book(db.Document):
    title = db.StringField(required=True)
    author = db.StringField(required=True)
    isbn = db.StringField()
    
    def json(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn
        }


class Review(db.Document):
    recommend = db.BooleanField(default=False)
    text = db.StringField()
    book = db.ReferenceField('Book')
    
    def json(self):
        return {
            'id': str(self.id),
            'recommend': self.recommend,
            'text': self.text,
            'book': str(self.book.id)
        }

