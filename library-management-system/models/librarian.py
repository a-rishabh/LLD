from models.member import Member
from models.book_item import BookItem

class Librarian(Member):
    def __init__(self, member_id: str, name: str):
        super().__init__(member_id, name)

    def add_book_item(self, library, book_item: BookItem):
        library.add_book_item(book_item)
        print(f"📘 Added book '{book_item.book.title}' to library.")

    def remove_book_item(self, library, book_item: BookItem):
        library.remove_book_item(book_item)
        print(f"🗑️ Removed book '{book_item.book.title}' from library.")

    def block_member(self, member: Member):
        member.account_status = member.account_status.BLACKLISTED
        print(f"🚫 Member '{member.name}' has been blacklisted.")
