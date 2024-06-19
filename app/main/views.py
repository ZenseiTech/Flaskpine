"""Views from main."""

from flask import render_template, request

from app import db
from app import logging as logger
from app.models import Author, Book

from . import main


def get_books():
    """Return the books."""
    return (
        db.session.query(Book, Author).filter(Book.author_id == Author.author_id).all()
    )


@main.route("/", methods=["GET"])
def home():
    """Start get endpoint."""
    return render_template("index.html", books=get_books())


@main.route("/submit", methods=["POST"])
def submit():
    """Submission of a book."""
    title = request.form["title"]
    author_name = request.form["author"]

    author_exists = db.session.query(Author).filter(Author.name == author_name).first()
    logger.debug(author_exists)

    # check if author already exists in db
    if author_exists:
        author_id = author_exists.author_id
        book = Book.query.filter_by(author_id=author_id).first()
        book.title = title
        db.session.commit()
    else:
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(author_id=author.author_id, title=title)
        db.session.add(book)
        db.session.commit()
    return render_template("index.html", books=get_books())


@main.route("/delete/<int:id>", methods=["DELETE"])
def delete_book(id):
    """Delete book by the passed id."""
    book = Book.query.get(id)
    author = Author.query.filter_by(author_id=book.author_id).first()
    if author:
        db.session.delete(author)
    db.session.delete(book)
    db.session.commit()

    return render_template("index.html", books=get_books())


@main.route("/get-edit-form/<int:id>", methods=["GET"])
def get_edit_form(id):
    """Edit a book by passed id."""
    book = Book.query.get(id)
    author = Author.query.get(book.author_id)

    return render_template("edit.html", book=book, author=author, id=id)


@main.route("/update/<int:id>", methods=["PUT"])
def update_book(id):
    """Upate book by id."""
    db.session.query(Book).filter(Book.book_id == id).update(
        {"title": request.form["title"]}
    )
    db.session.commit()

    return render_template("table-body.html", books=get_books())
