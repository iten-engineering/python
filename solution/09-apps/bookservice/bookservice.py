from flask import Flask, abort, request, jsonify
from books import Books

# -----------------------------------------------------------------------------
# Simple flask sample.
# For a good introduction see https://flask.palletsprojects.com
# -----------------------------------------------------------------------------

#
# initailize
#
app = Flask(__name__,
    static_url_path='',
    static_folder='static')

books = Books()

#
# error handlers
#
@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('404.html'), 404


#
# request handlers
#
@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route("/echo")
def echo():
    return jsonify(dict(request.headers))


@app.route("/books")
def list_books():
    return books.get_books()


@app.route("/book/<isbn>")
def list_book(isbn):
    try:
        return books.get_book(isbn)
    except Exception as e:
        abort(404, description="not found")
