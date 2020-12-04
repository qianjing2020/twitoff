# web_app/routes/book_routes.py

from web_app.models import parse_records
from flask import Blueprint, jsonify, request, render_template, flash, redirect
from web_app.models import Book, db, parse_records

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    # books = [
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 2, "title": "Book 2"},
    #     {"id": 3, "title": "Book 3"},
    # ]       
   
    book_records = Book.query.all() # SELECT * FROM books
    print(book_records)
    books = parse_records(book_records)
    return jsonify(books)
    

@book_routes.route("/books")
def list_books_for_humans():
    book_records = Book.query.all()
    books = parse_records(book_records)
    return render_template("books.html", message="Here are existing books in our database: ", books=books)


@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")


@book_routes.route("/books/create", methods=["POST"])
def create_book():
    book_by_form = dict(request.form)
    print("FORM DATA:", book_by_form)
    
    # add new book to database
    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()

    """return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": book_by_form
    })"""
    flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect(f"/books")
