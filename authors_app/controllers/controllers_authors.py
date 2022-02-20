from authors_app import app
from flask import render_template, redirect, request, session
from authors_app.models.authors import Author
from authors_app.models.books import Book

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    author = {
        'fname': request.form['fname'],
        'lname': request.form['lname']
    }
    new_id = Author.save(author)
    return redirect(f"/show/{new_id}")

@app.route('/show')
def show_all():
    return render_template('/results.html', authors = Author.show_all())

@app.route('/show/<int:id>')
def show_record(id):
    author_id = {
        'id': id
    }
    return render_template("/details.html", author = Author.show(author_id))

@app.route('/edit/<int:id>')
def edit(id):
    author_id = {
        'id': id
    }
    return render_template("edit.html", author = Author.show(author_id))

@app.route('/update/<int:id>') 
def update(id):
    author = {
        'id': id,
        "fname": request.form['fname'],
        "lname": request.form['lname']
    }
    Author.update(author)
    return redirect(f"/show/{id}")

@app.route('/delete/<int:id>') 
def delete(id):
    author = {
        'id': id,
    }
    Author.delete(author)
    return redirect('/show')

@app.route('/add_author', methods=['POST'])
def add_author():
    favorite = {
        'auth_id': request.form['auth_id'],
        'book_id': request.form['book_id']
    }
    Book.favorite(favorite)
    return redirect(f"/favorited_by/{ request.form['book_id'] }")