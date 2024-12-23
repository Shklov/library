import unittest
from unittest.mock import patch
from src.services.book_service import BookService


class TestBookService(unittest.TestCase):

    def setUp(self):
        # Reset the in-memory "database" before each test
        global books_dict
        books_dict = {}

    @patch('src.repository.simple_cache_db.get_books', return_value={})
    def test_add_book(self, mock_get_books):
        book_data = {
            "isbn": "1234567890123",
            "title": "Test Book",
            "author": "Test Author",
            "publisher": "Test Publisher",
            "publication_date": "2024-12-23"
        }

        # Mock the add_book function to avoid interacting with the actual repository
        with patch('src.repository.simple_cache_db.add_book') as mock_add_book:
            mock_add_book.return_value = None  # Simulate successful addition
            result, status_code = BookService.add_book(book_data)

            self.assertEqual(status_code, 201)
            self.assertEqual(result["isbn"], "1234567890123")
            self.assertEqual(result["title"], "Test Book")

if __name__ == '__main__':
    unittest.main()
