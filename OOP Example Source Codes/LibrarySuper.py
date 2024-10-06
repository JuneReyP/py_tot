class Book:
    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.pub_year}")

class EBook(Book):
    def __init__(self, title, author, pub_year, file_size):
        super().__init__(title, author, pub_year)
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size} MB")

class PrintedBook(Book):
    def __init__(self, title, author, pub_year, nopages):
        super().__init__(title, author, pub_year)
        self.nopages = nopages

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.nopages}")

ebook = EBook("Python", "Juan Cruz", 2024, 50)
printed_book = PrintedBook("Java", "James Gosling", 2024, 200)

print("EBook Info:")
ebook.display_info()
print("\nPrinted Book Info:")
printed_book.display_info()