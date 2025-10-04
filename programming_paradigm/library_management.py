class Book:
    def __init__(self, title, author, _is_checked_out = False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def check_out_book(self):
        self._is_checked_out = True
        
    def return_book(self):
        self._is_checked_out = False
       
    

class Library:
    def __init__(self, _books):
        if _books is None:
            self._books = []
        else:
            self._books = _books
    def add_book(self, book):
        self._books.append(book)
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out_book()
                break
            else:
                book._is_checked_out()     
    def list_available_books(self):