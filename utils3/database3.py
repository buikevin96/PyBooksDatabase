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

def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # [(name, author, read), (name, author, read)]

    connection.commit()
    connection.close()

    return books

def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    connection.commit()
    connection.close()

def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))

    connection.commit()
    connection.close()
