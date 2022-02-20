from authors_app import app
from flask import render_template, redirect, request, session
from authors_app.models.books import Book
from authors_app.models.authors import Author

@app.route('/create_book', methods=["POST"])
def new_book():
    book = {
        'title': request.form['title'],
        'pages': request.form['pages'],
    }
    new_book_id = Book.save(book)
    print(new_book_id)
    fave = {
        'book_id': new_book_id,
        'auth_id': request.form['auth_id']
    }
    Book.favorite(fave)
    return redirect(f"/books/{ request.form['auth_id'] }")

@app.route('/books/<int:id>')
def show_faves(id):
    author_id = {
        'id': id
    }
    books = Book.show_limited(author_id)
    return render_template('books.html', author = Author.show(author_id), auth_books = Author.show_faves(author_id), books = books)

@app.route('/add_book', methods=['POST'])
def add_fave():
    fave = {
        'book_id': request.form['book_id'],
        'auth_id': request.form['auth_id']
    }
    Book.favorite(fave)
    return redirect(f"/books/{ request.form['auth_id'] }")

@app.route('/favorited_by/<int:id>')
def favorited_by(id):
    book_id = {
        'id': id
    }
    authors = Author.show_limited(book_id)
    return render_template('/book_details.html', favorites = Book.show_faved(book_id), book = Book.show(book_id), authors = authors)