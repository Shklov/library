books_dict = {}  # This will act as an in-memory "database", a simple dictionary with isbn key.
# Note: the filter by author will have bad performance without an "index", I kept it that way for simplicity.

def get_books():
    return books_dict

def get_book_by_isbn(isbn):
    return books_dict.get(isbn)

def add_book(book):
    if book.isbn in books_dict:
        raise ValueError(f"Book with ISBN {book.isbn} already exists")
    books_dict[book.isbn] = book.to_dict()

def delete_book(isbn):
    if isbn not in books_dict:
        raise ValueError("Book not found")
    del books_dict[isbn]

def update_book(isbn, book_data):
    if isbn not in books_dict:
        raise ValueError("Book not found")
    books_dict[isbn].update(book_data)

def exists(isbn):
    return isbn in books_dict
