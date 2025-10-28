from datetime import date
from enums.book_status import BookStatus
from models.book import Book

class BookItem:
    def __init__(self, barcode: str, book: Book, rack: str, publication_date: date):
        self.barcode = barcode
        self.book = book
        self.rack = rack
        self.publication_date = publication_date
        self.status = BookStatus.AVAILABLE
        self.borrowed_by = None  # Will store Member object when checked out

    def checkout(self, member):
        if self.status != BookStatus.AVAILABLE:
            print(f"❌ Book '{self.book.title}' not available for checkout.")
            return False
        self.status = BookStatus.LOANED
        self.borrowed_by = member
        print(f"✅ Book '{self.book.title}' checked out by {member.name}")
        return True

    def return_book(self):
        if self.status != BookStatus.LOANED:
            print(f"⚠️ Book '{self.book.title}' is not currently loaned.")
            return False
        self.status = BookStatus.AVAILABLE
        self.borrowed_by = None
        print(f"📚 Book '{self.book.title}' returned successfully.")
        return True

    def __repr__(self):
        return f"<BookItem {self.book.title} | {self.barcode} | {self.status.value}>"
