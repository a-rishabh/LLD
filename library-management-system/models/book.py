from typing import List

class Book:
    def __init__(self, isbn: str, title: str, subject: str, authors: List[str]):
        self.isbn = isbn
        self.title = title
        self.subject = subject
        self.authors = authors

    def __repr__(self):
        return f"<Book {self.title} ({self.isbn})>"
