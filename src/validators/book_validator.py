import re


def validate_isbn(isbn):
    """Validate ISBN format (13 digits)."""
    if not re.match(r"^\d{13}$", isbn):
        raise ValueError("Invalid ISBN format. ISBN must be 13 digits.")

def validate_book_data(book_data):
    """Validate input data for a new book."""
    if not book_data.get("isbn"):
        raise ValueError("ISBN is required")
    validate_isbn(book_data["isbn"])

    if not book_data.get("title"):
        raise ValueError("Title is required")

    if not book_data.get("author"):
        raise ValueError("Author name is required")

    if not book_data.get("publisher"):
        raise ValueError("Publisher name is required")

    if not book_data.get("publication_date"):
        raise ValueError("Publication date is required")