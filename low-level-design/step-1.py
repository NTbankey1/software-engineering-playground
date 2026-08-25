class Book:
    def __init__(self, title: str):
        self.title = title
        self.is_borrowed = False

class Memeber:
    def __init__(self, name: str):
        self.name = name

    def borrow(self, book: Book):
        if book.is_borrowed:
            print("sach da muon")

            return
        book.is_borrowed = True
        print(f"{self.name} da muon {book.title}")

    def return_book(self, book: Book):
        book.is_borrowed = False
        print(f"{self.name} da tra {book.title}")

class Library:
    def __init__(self):
        self.books = []

    def search_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        return None

library = Library()
book = Book("clean code")
member = Memeber("bao")

library.books.append(book)
member.borrow(book)
member.borrow(book)

member.return_book(book)
