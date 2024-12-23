from flask import Blueprint, request, jsonify
from src.services.book_service import BookService

"""
book_controller.py

This module handles the routes and logic related to book management, including 
adding, updating, deleting, and retrieving books from the system. It defines
the controller functions that are used by the web application.


Routes:
    - add_book parameter: Adds a new book to the system. 
      POST /books
    - get_book parameter: <isbn>: Retrieves a book by its ISBN.
      GET /books/<isbn>
    - list_books parameter: Retrieves a list of all books in the system. (Optional argument: Author to filter by)
      GET /books
    - update_book parameter: <isbn>: Updates a book's information by its ISBN.
      PUT /books/<isbn>
    - delete_book parameter: <isbn>: Deletes a book by its ISBN.
      DELETE /books/<isbn>
"""

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['POST'])
def add_book():
    """
    - add_book parameter: Adds a new book to the library.
      POST /books

        Request body:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - isbn (str): The ISBN number of the book.
        - publisher (str): The publisher of the book.
        - publication_date (str): The publication date of the book in YYYY-MM-DD format.

    Returns:
        - JSON response with status code:
            - 201 if the book is added successfully.
            - 400 if validation fails.
            - 409 if the book already exists.
    """
    book_data = request.get_json()
    result, status = BookService.add_book(book_data)
    return jsonify(result), status

@book_bp.route('/books', methods=['GET'])
def list_books():
    author = request.args.get('author')
    result, status = BookService.list_books(author)
    return jsonify(result), status

@book_bp.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    result, status = BookService.get_book(isbn)
    return jsonify(result), status

@book_bp.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    update_data = request.get_json()
    result, status = BookService.update_book(isbn, update_data)
    return jsonify(result), status

@book_bp.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    result, status = BookService.delete_book(isbn)
    return jsonify(result), status
