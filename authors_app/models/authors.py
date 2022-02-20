from authors_app.config.mysqlconnection import connectToMySQL

DB = 'authors_and_books'

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%(fname)s, %(lname)s);"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM authors;"
        authors_from_db = connectToMySQL(DB).query_db(query)
        print(authors_from_db)
        all_authors = []
        for author in authors_from_db:
            all_authors.append(cls(author))
        return all_authors

    @classmethod
    def show_limited(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT authors.id FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s);"
        books_from_db = connectToMySQL(DB).query_db(query,data)
        limited_books = []
        for book in books_from_db:
            limited_books.append(cls(book))
        return limited_books

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM authors WHERE authors.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        author = cls(result[0])
        return author

    @classmethod
    def update(cls,data):
        query = "UPDATE authors SET first_name=%(fname)s, last_name=%(lname)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def show_faves(cls,data):
        query = "SELECT authors.first_name, authors.last_name, books.title, books.num_of_pages FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        return results