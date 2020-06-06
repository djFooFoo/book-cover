import base64

import flask
import requests

import book_cover

bookCover = book_cover.BookCover(requests)
bookCoverApplication = flask.Flask(__name__)


@bookCoverApplication.route("/book-cover/<isbn>")
def get_book_cover(isbn: str):
    print(f'Retrieving image via isbn `{isbn}`')
    img = None
    try:
        img = bookCover.get_by(isbn)
    except RuntimeError as error:
        print(error)
        flask.abort(404, error)
    return base64.b64encode(img), 200


if __name__ == "__main__":
    from waitress import serve

    serve(bookCoverApplication, host="0.0.0.0", port=10000)
