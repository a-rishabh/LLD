from datetime import date, timedelta
from models.book_item import BookItem

class BookLending:
    BORROW_DAYS = 14  # standard due window (2 weeks)

    def __init__(self, book_item: BookItem, member_id: str):
        self.book_item = book_item
        self.member_id = member_id
        self.issue_date = date.today()
        self.due_date = self.issue_date + timedelta(days=BookLending.BORROW_DAYS)
        self.return_date = None

    