from flask import Blueprint, jsonify

book_routes = Blueprint("book_routes", __name__)

@book_routes.route('/books.json')
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"}
    ]
    return jsonify(books)