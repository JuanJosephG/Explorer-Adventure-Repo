class Book():
    def __init__(self, title, Author, Isbn, Genre, Copies):                 #BookClass
        self.Title = title
        self.Author = Author
        self.Isbn = Isbn
        self.Genre = Genre
        self.Copies = Copies

        #Author Class
class Author():
    def __init__(self, Auth_name, Auth_birthday , Auth_nationality):
        self.Auth_name = Auth_name
        self.Auth_birthday = Auth_birthday
        self.Auth_nationality = Auth_nationality
        
        #library Class Catalog
class LibraryCatalog():
    def __init__(self):
        self.Book = []       #empty list to store books
      
    def Book_add(self, title, Author, Isbn, Genre, Copies):
        New_book = Book(title, Author, Isbn, Genre, Copies)
        self.Book.append(New_book)   #adding book to list
        print("book added")

    def Book_remove(self, title):
        for Book in self.Book:
            if Book.Title  == title:
                self.Book.remove(Book)  #remove book from list
                print("Book has been removed")
    def Book_display(self):
            for Book in self.Book:
                print(f"Title:{Book.Title}, Author:{Book.Author.Auth_name}, ISBN:{Book.Isbn}, Genre:{Book.Genre}, Copies:{Book.Copies}")
    def Book_search(self, title):
        for Book in self.Book:
            if Book.Title == title: 
                print(f"Title:{Book.Title}, Author:{Book.Author.Auth_name}, ISBN:{Book.Isbn}, Genre:{Book.Genre}, Copies:{Book.Copies}")
        
        #user Interactions

Library_catalog = LibraryCatalog()

#adding Books
Library_catalog.Book_add("Python", Author("Snake", "1900-01-1", "USA"), "123-1-12-123456-1", "Programming", 4)
Library_catalog.Book_add("Dragons", Author("Sam", "1950-01-11", "UK"), "321-1-12-123456-1", "Fiction", 2)
Library_catalog.Book_add("Eating Food", Author("Donald", "1960-02-15", "USA"),"321-2-14-145267-1","Culinary", 10)

#removing book
Library_catalog.Book_remove("Python")
#display all books
Library_catalog.Book_display()
#Search Book 
Library_catalog.Book_search("Dragons")

