class Book:
    def __init__(self, isbn, title, author, publisher, publication_date):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "publication_date": self.publication_date
        }