import json
"""
Concerned with storing and retrieving books from a json file.

[
    {
        'name': 'Clean Code',
        'author': 'Robert',
        'read': True
    }
]
"""

books_file = 'books.json'

def create_book_table():
    with open('books_file', 'w') as file:
        json.dump([], file)

def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)

# Opens file, delete all contents, goes through all of items in parameter, and types it in csv format
def _save_all_books(books):
    with open('books_file', 'w') as file:
        json.dump(books, file)

def get_all_books():
    #opens the file
    with open('books_file', 'r') as file:
        return json.load(file)

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
