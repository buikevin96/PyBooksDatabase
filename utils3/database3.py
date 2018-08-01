import sqlite3
"""
Concerned with storing and retrieving books from a database.

"""

books_file = 'books.json'

def create_book_table():
    connection = sqlite3.connect('data.db') # Connect to database
    cursor = connection.cursor()

    #Query to create our table
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text, author text, read integer)')

    connection.commit()
    connection.close() # Close the connection

def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()

# Opens file, delete all contents, goes through all of items in parameter, and types it in csv format
def _save_all_books(books):
    with open('books_file', 'w') as file:
        json.dump(books, file)

def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall() # [(name, author, read), (name, author, read)]

    connection.close()

    return books

def mark_book_as_read(name):
    books = get_all_books() # Read all the books
    # Modify the book we want
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books) # Saves them all back


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

