# Classes: Book (ID, isRented), User (ID, [rentedBooks]), Library ([{BooksAvail:1/0}])

class Book():
    def __init__(self, book_ID):
        self.book_ID = book_ID
        self.isRented = 0
    
class User():
    def __init__(self,user_ID):
        self.user_ID = user_ID
        self.booksRented = []

class Library():
    def __init__(self, name, availableBooks):
        self.name = name
        self.availableBooks = availableBooks #[of objects]
    
    def checkBooks(self):
        bookList = []
        for b in self.availableBooks:
            bookList.append(b.book_ID)
        print(bookList)
    



book1 = Book(1) 
book2 = Book(2)
book3 = Book(3)

user1 = User(10)
user2 = User(20)
user3 = User(30)

library1 = Library('British Library',[book1,book2,book3])
print(library1.availableBooks)
library1.checkBooks()



n, 1
n2, 1
