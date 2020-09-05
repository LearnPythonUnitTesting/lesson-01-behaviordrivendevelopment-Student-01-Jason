class Librarian:
    books = ['The Shadow', 'Mirror Mine']

    def borrow(self, name):
        self.books.remove(name)

    def returnBook(self, name):
        self.books.append(name)
