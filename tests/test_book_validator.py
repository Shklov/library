import unittest
from src.validators.book_validator import validate_isbn, validate_book_data

# A mock of books_dict to use in the tests
books_dict = {}

class TestBookValidator(unittest.TestCase):

    def test_validate_isbn_valid(self):
        """Test valid ISBN numbers."""
        try:
            validate_isbn("1234567890123")  # Valid ISBN
        except ValueError as e:
            self.fail(f"validate_isbn raised ValueError unexpectedly: {str(e)}")

    def test_validate_isbn_invalid(self):
        """Test invalid ISBN numbers (not 13 digits)."""
        with self.assertRaises(ValueError):
            validate_isbn("123456789012")  # Too short
        with self.assertRaises(ValueError):
            validate_isbn("12345678901234")  # Too long
        with self.assertRaises(ValueError):
            validate_isbn("abcde12345678")  # Non-numeric

    def test_validate_book_data_valid(self):
        """Test valid book data."""
        valid_book_data = {
            "isbn": "1234567890123",
            "title": "Valid Book",
            "author": "Valid Author",
            "publisher": "Valid Publisher",
            "publication_date": "2024-01-01"
        }
        try:
            validate_book_data(valid_book_data)  # Should not raise any exceptions
        except ValueError as e:
            self.fail(f"validate_book_data raised ValueError unexpectedly: {str(e)}")

    def test_validate_book_data_missing_isbn(self):
        """Test missing ISBN in the book data."""
        invalid_book_data = {
            "title": "Missing ISBN Book",
            "author": "Author",
            "publisher": "Publisher",
            "publication_date": "2024-01-01"
        }
        with self.assertRaises(ValueError) as context:
            validate_book_data(invalid_book_data)
        self.assertEqual(str(context.exception), "ISBN is required")

    def test_validate_book_data_invalid_isbn(self):
        """Test invalid ISBN format in the book data."""
        invalid_book_data = {
            "isbn": "1234567890",  # Invalid ISBN (not 13 digits)
            "title": "Invalid ISBN Book",
            "author": "Author",
            "publisher": "Publisher",
            "publication_date": "2024-01-01"
        }
        with self.assertRaises(ValueError) as context:
            validate_book_data(invalid_book_data)
        self.assertEqual(str(context.exception), "Invalid ISBN format. ISBN must be 13 digits.")

    def test_validate_book_data_missing_title(self):
        """Test missing title in the book data."""
        invalid_book_data = {
            "isbn": "1234567890123",
            "author": "Author",
            "publisher": "Publisher",
            "publication_date": "2024-01-01"
        }
        with self.assertRaises(ValueError) as context:
            validate_book_data(invalid_book_data)
        self.assertEqual(str(context.exception), "Title is required")

    def test_validate_book_data_missing_author(self):
        """Test missing author in the book data."""
        invalid_book_data = {
            "isbn": "1234567890123",
            "title": "Book Without Author",
            "publisher": "Publisher",
            "publication_date": "2024-01-01"
        }
        with self.assertRaises(ValueError) as context:
            validate_book_data(invalid_book_data)
        self.assertEqual(str(context.exception), "Author name is required")

    def test_validate_book_data_missing_publisher(self):
        """Test missing publisher in the book data."""
        invalid_book_data = {
            "isbn": "1234567890123",
            "title": "Book Without Publisher",
            "author": "Author",
            "publication_date": "2024-01-01"
        }
        with self.assertRaises(ValueError) as context:
            validate_book_data(invalid_book_data)
        self.assertEqual(str(context.exception), "Publisher name is required")

    def test_validate_book_data_missing_publication_date(self):
        """Test missing publication date in the book data."""
        invalid_book_data = {
            "isbn": "1234567890123",
            "title": "Book Without Date",
            "author": "Author",
            "publisher": "Publisher"
        }
        with self.assertRaises(ValueError) as context:
            validate_book_data(invalid_book_data)
        self.assertEqual(str(context.exception), "Publication date is required")


if __name__ == '__main__':
    unittest.main()
