"""Database models."""
from . import db


class Author(db.Model):
    """Author model."""

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", backref="author")

    def __repr__(self):
        """Return the object representation."""
        return "<Author: {}>".format(self.books)


class Book(db.Model):
    """Book model."""

    book_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.author_id"))
    title = db.Column(db.String)
