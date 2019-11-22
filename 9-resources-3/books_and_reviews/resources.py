from flask import request
from flask_restful import Resource, abort
from books_and_reviews import models
import json


class Index(Resource):
    def get(self):
        return { 'message': 'Books & Reviews API is running' }


class Books(Resource):
    def get(self):
        books = models.Book.objects
        books = [b.json() for b in books]
        return { 'message': 'Found books', 'data': books }

    def post(self):
        data = request.json
        print(data)
        
        title = data.get('title')
        author = data.get('author')
        isbn = data.get('isbn')
        
        book = models.Book(title=title, author=author, isbn=isbn).save()
        return { 'message': 'Created a new book', 'data': book.json() }



class Book(Resource):
    def get(self, id):
        book = models.Book.objects(id=id).first()
        if not book:
            abort(404)
        return { 'message': 'Found a book', 'data': book.json() }

    def delete(self, id):
        book = models.Book.objects(id=id).first()
        if not book:
            abort(404)
        book.delete()
        return { 'message': 'Deleted the book' }



class Reviews(Resource):
    def get(self, book_id):
        book = models.Book.objects(id=book_id).first()
        reviews = models.Review.objects(book = book_id)
        
        reviews = [r.json() for r in reviews]
        
        return { 'message': 'Found reviews for book {}'.format(book_id), 'data': reviews }

    def post(self, book_id):
        review = None
        book = models.Book.objects(id=book_id).first()
        if not book:
            abort(404)
        
        data = request.json
        
        recommend = data.get('recommend')
        text = data.get('text')
        
        if recommend is None:
            abort(400)
        
        review = models.Review(recommend=recommend, text=text, book=book).save()
        
        return { 'message': 'Created a new review for book {}'.format(book_id), 'data': review.json() }


class Review(Resource):
    def get(self, id):
        review = models.Review.objects(id=id).first()
        if not review:
            abort(404)
        return { 'message': 'Found a review', 'data': review.json() }

    def patch(self, id):
        review = models.Review.objects(id=id).first()
        if not review:
            abort(404)
        
        data = request.json
        
        recommend = data.get('recommend')
        text = data.get('text')
        
        if recommend is not None:
            review.recommend = recommend
        if text:
            review.text = text
        
        review.save()
        
        return { 'message': 'Updated the review', 'data': review.json() }

    def delete(self, id):
        review = models.Review.objects(id=id).first()
        if not review:
            abort(404)
        review.delete()
        return { 'message': 'Deleted the review', 'data': id }
