"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:

name, author, read\n
name, author, read\n
name, author, read\n
"""

books_file = 'books.txt'

def add_book(name, author):
    with open('books_file', 'a') as file:
        file.write(f'{name},{author},0')
    books.append({'name': name, 'author': author, 'read': False})

def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

def delete_book(name):
    global books # Uses books that is not local
    books_new = [book for book in books if book['name'] != 'name'] # Add each book to new list if book['name'] != name

    for book in books:
        if book['name'] == name:
            books.remove(book)

