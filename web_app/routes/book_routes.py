from flask import Blueprint, jsonify, render_template

book_routes = Blueprint("book_routes", __name__)

@book_routes.route('/books.json')
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"}
    ]
    return jsonify(books)

@book_routes.route('/books')
def list_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"}
    ]
    return render_template("books.html", message="Here's some books", books=books)


@book_routes.route('/new_book')
def create_book():
    return render_template("new_book.html")


