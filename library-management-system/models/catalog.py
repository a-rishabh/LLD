from typing import List, Dict
from models.book_item import BookItem

class Catalog:
    def __init__(self):
        self.books_by_title: Dict[str, List[BookItem]] = {}
        self.books_by_author: Dict[str, List[BookItem]] = {}
        self.books_by_subject: Dict[str, List[BookItem]] = {}

    def add_book_item(self, book_item: BookItem):
        # index by title
        title = book_item.book.title.lower()
        self.books_by_title.setdefault(title, []).append(book_item)

        # index by authors
        for author in book_item.book.authors:
            author_key = author.lower()
            self.books_by_author.setdefault(author_key, []).append(book_item)

        # index by subject
        subject_key = book_item.book.subject.lower()
        self.books_by_subject.setdefault(subject_key, []).append(book_item)

    def remove_book_item(self, book_item: BookItem):
        title = book_item.book.title.lower()
        if title in self.books_by_title and book_item in self.books_by_title[title]:
            self.books_by_title[title].remove(book_item)

        for author in book_item.book.authors:
            author_key = author.lower()
            if author_key in self.books_by_author and book_item in self.books_by_author[author_key]:
                self.books_by_author[author_key].remove(book_item)

        subject_key = book_item.book.subject.lower()
        if subject_key in self.books_by_subject and book_item in self.books_by_subject[subject_key]:
            self.books_by_subject[subject_key].remove(book_item)

    def search_by_title(self, title: str) -> List[BookItem]:
        return self.books_by_title.get(title.lower(), [])

    def search_by_author(self, author: str) -> List[BookItem]:
        return self.books_by_author.get(author.lower(), [])

    def search_by_subject(self, subject: str) -> List[BookItem]:
        return self.books_by_subject.get(subject.lower(), [])

    def display_results(self, book_items: List[BookItem]):
        if not book_items:
            print("❌ No matching books found.")
            return
        for item in book_items:
            print(f"📗 {item.book.title} by {', '.join(item.book.authors)} "
                  f"({item.status.value}) | Barcode: {item.barcode}")
