from authors_app.config.mysqlconnection import connectToMySQL

DB = 'authors_and_books'

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(pages)s);"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM books;"
        books_from_db = connectToMySQL(DB).query_db(query)
        all_books = []
        for book in books_from_db:
            all_books.append(cls(book))
        return all_books

    @classmethod
    def show_limited(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN (SELECT books.id FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s);"
        books_from_db = connectToMySQL(DB).query_db(query,data)
        limited_books = []
        for book in books_from_db:
            limited_books.append(cls(book))
        return limited_books

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM books WHERE books.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        book = cls(result[0])
        return book

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def show_faved(cls,data):
        query = "SELECT title, authors.id, authors.first_name, authors.last_name FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def favorite(cls,data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(auth_id)s, %(book_id)s);"
        return connectToMySQL(DB).query_db(query,data)