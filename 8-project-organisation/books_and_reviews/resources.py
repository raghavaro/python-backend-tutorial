from flask_restful import Resource


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
