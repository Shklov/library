from src.models.book import Book
from src.validators.book_validator import validate_book_data
from src.repository.simple_cache_db import add_book, get_book_by_isbn, get_books, delete_book, update_book, exists

class BookService:

    @staticmethod
    def add_book(book_data):
        try:
            validate_book_data(book_data)
            if exists(book_data["isbn"]):
                return {"error": f"Book with ISBN {book_data['isbn']} already exists"}, 409
            book = Book(**book_data)
            add_book(book)
            return book.to_dict(), 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @staticmethod
    def list_books(author=None):
        books = get_books()
        if author:
            filtered_books = [book for book in books.values() if book['author'].lower() == author.lower()]
            return filtered_books, 200
        return list(books.values()), 200

    @staticmethod
    def get_book(isbn):
        book = get_book_by_isbn(isbn)
        if book:
            return book, 200
        return {"message": "Book not found"}, 404

    @staticmethod
    def update_book(isbn, update_data):
        try:
            validate_book_data(update_data)
            update_book(isbn, update_data)
            return update_data, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    @staticmethod
    def delete_book(isbn):
        try:
            delete_book(isbn)
            return {"message": "Book deleted successfully"}, 200
        except ValueError as e:
            return {"message": str(e)}, 404