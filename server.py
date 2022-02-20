from authors_app import app
from authors_app.controllers import controllers_authors
from authors_app.controllers import controllers_books

if __name__ == '__main__':
    app.run(debug=True)
