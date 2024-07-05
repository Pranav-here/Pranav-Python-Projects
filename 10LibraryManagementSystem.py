# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and show how you can
# print all books, add a book and get the number of books using different methods.
# Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self, books, add_book):
        self.books = books
        self.add = add_book

    def Book_names(self):
        return self.books
        # for i in range(len(self.books)):
        #     print(self.books[i])

    def add_book(self):
        self.books.append(self.add)

    def number_of_books(self):
        return len(self.books)


add_book = "NewBook"
books = ["Book1", "Book2", "Book3", "Book4", "Book5"]


book = Library(books, add_book)
print(book.Book_names())
print(book.number_of_books())

book.add_book()
print(book.Book_names())

