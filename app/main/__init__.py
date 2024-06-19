"""Main blueprint."""
from flask import Blueprint


def do_import():
    """Trick to bypass git_commit error of being imported by unused."""
    from . import views

    views.logger


main = Blueprint("main", __name__)
do_import()
