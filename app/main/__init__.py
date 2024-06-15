"""Main blueprint."""
from flask import Blueprint


def do_import():
    """Trick to bypass git_commit error ..."""
    from . import views

    views.logger


main = Blueprint("main", __name__)
do_import()
