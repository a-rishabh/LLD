from enums.account_status import AccountStatus
from models.book_item import BookItem

class Member:
    MAX_BOOKS_ALLOWED = 5  # configurable limit

    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.account_status = AccountStatus.ACTIVE
        self.borrowed_books = []  # list of BookItem objects

    def borrow_book(self, book_item: BookItem):
        if self.account_status != AccountStatus.ACTIVE:
            print(f"🚫 Member {self.name} is not active.")
            return False

        if len(self.borrowed_books) >= Member.MAX_BOOKS_ALLOWED:
            print(f"⚠️ {self.name} reached borrow limit ({Member.MAX_BOOKS_ALLOWED}).")
            return False

        if book_item.checkout(self):
            self.borrowed_books.append(book_item)
            return True
        return False

    def return_book(self, book_item: BookItem):
        if book_item not in self.borrowed_books:
            print(f"❌ {self.name} didn’t borrow '{book_item.book.title}'.")
            return False

        if book_item.return_book():
            self.borrowed_books.remove(book_item)
            return True
        return False

    def __repr__(self):
        return f"<Member {self.name} | Books borrowed: {len(self.borrowed_books)}>"
