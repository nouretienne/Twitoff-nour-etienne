from flask import Blueprint, jsonify, render_template, request, flash, redirect
from web_app.models import db, Book, parse_records


book_routes = Blueprint("book_routes", __name__)

@book_routes.route('/books.json')
def list_books():
    #books = [
    #    {"id": 1, "title": "Book 1"},
    #    {"id": 2, "title": "Book 2"},
    #    {"id": 3, "title": "Book 3"}
    #]
    book_records = Book.query.all()
    print(book_records)
    books_response = parse_records(book_records)
    return jsonify(books_response)

@book_routes.route('/books')
def list_for_humans():
    #books = [
    #    {"id": 1, "title": "Book 1"},
    #    {"id": 2, "title": "Book 2"},
    #    {"id": 3, "title": "Book 3"}
    #]
    book_records = Book.query.all()
    print(book_records)
    #breakpoint()
    return render_template("books.html", message="Here's some books", books=book_records)


@book_routes.route('/books/new')
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create",methods=["POST"])
def create_book():
    print("FORM DATA:",dict(request.form))

    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    print('ok')
    db.session.add(new_book)
    db.session.commit()

    #return jsonify({"message":"BOOK CREATED OK TODO",
    #                "book": dict(request.form)
    #})
    flash(f"Book '{new_book.title}' created successfully", "danger")
    return redirect(f"/books")

