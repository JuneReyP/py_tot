class Book:
    def __init__(self, title, author, publication_year):
        self._title = title
        self._author = author
        self._publication_year = publication_year

    def display_info(self):
        print("Title:", self._title)
        print("Author:", self._author)
        print("Publication Year:", self._publication_year)

class EBook(Book):
    __file_size = 10
    __format = "PDF"

    def display_info(self):
        Book.display_info(self)
        print("File Size:", self.__file_size)
        print("Format:", self.__format)

class PrintedBook(Book):
    __number_of_pages = 100
    def display_info(self):
        Book.display_info(self)
        print("Number of Pages:", self.__number_of_pages)

print("======From Book class========")
book = Book("Python Programming", "John Doe", 2020)
book.display_info()
print("=============================")
print("======From EBook class========")
ebook = EBook()
ebook.display_info()
print("=============================")
print("======From PrintedBook class========")
printedbook = PrintedBook()
printedbook.display_info()
print("=============================")