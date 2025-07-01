"""Write a python program to create a book class declare the states as
Book name , Author name, Publisher name, Published date, category of book
i) Create 5 objects & initialize the values using constructor where out of 5
create  1st object using one parameterized constructor
create  2nd object using two parameterized constructors
create  3rd object using zero parameterized constructor
create  4th object using four parameterized constructors
create  5th object using four parameterized constructors
Access the values using Accessor methods
Update the values using mutator method for name of the book"""
class Book:
    def __init__(self):
        self.book_name = "Unknown"
        self.author_name = "Unknown"
        self.publisher_name = "Unknown"
        self.published_date = "Unknown"
        self.category = "Unknown"
    def __init__(self, book_name=None, author_name=None, publisher_name=None, published_date=None, category=None):
        self.book_name = book_name
        self.author_name = author_name
        self.publisher_name = publisher_name
        self.published_date = published_date
        self.category = category
    def __init__(self, book_name):
        self.book_name = book_name
        self.author_name = "Unknown"
        self.publisher_name = "Unknown"
        self.published_date = "Unknown"
        self.category = "Unknown"
    def __init__(self, book_name, author_name):
        self.book_name = book_name
        self.author_name = author_name
        self.publisher_name = "Unknown"
        self.published_date = "Unknown"
        self.category = "Unknown"
    def __init__(self, book_name, author_name, publisher_name, published_date):  
        self.book_name = book_name
        self.author_name = author_name
        self.publisher_name = publisher_name
        self.published_date = published_date
        self.category = "Unknown"
    def get_book_name(self):
        return self.book_name
    def get_author_name(self):
        return self.author_name
    def get_publisher_name(self):
        return self.publisher_name
    def get_published_date(self):
        return self.published_date
    def get_category(self):
        return self.category
    def set_book_name(self, book_name):
        self.book_name = book_name
    def set_author_name(self, author_name):
        self.author_name = author_name
    def set_publisher_name(self, publisher_name):
        self.publisher_name = publisher_name
    def set_published_date(self, published_date):
        self.published_date = published_date
    def set_category(self, category):
        self.category = category
book1 = Book("Python Programming")
book2 = Book("Data Science","John Doe")
book3 = Book()
book4 = Book("Machine Learning", "Jane Smith", "Tech Publishers", "2023-01-01")
book5 = Book("AI Fundamentals", "Alice Johnson", "Future Press", "2022-05-15", "Technology")
print("Book 1 Name:", book1.get_book_name())
print("Book 2 Author:", book2.get_author_name())
print("Book 3 Publisher:", book3.get_publisher_name())
print("Book 4 Published Date:", book4.get_published_date())
print("Book 5 Category:", book5.get_category())
book1.set_book_name("Advanced Python Programming")
print("Updated Book 1 Name:", book1.get_book_name())
if __name__ == "__main__":
    book1 = Book("Python Programming")
    book2 = Book("Data Science", "John Doe")
    book3 = Book()
    book4 = Book("Machine Learning", "Jane Smith", "Tech Publishers", "2023-01-01")
    book5 = Book("AI Fundamentals", "Alice Johnson", "Future Press", "2022-05-15", "Technology")
    print("Book 1 Name:", book1.get_book_name())
    print("Book 2 Author:", book2.get_author_name())
    print("Book 3 Publisher:", book3.get_publisher_name())
    print("Book 4 Published Date:", book4.get_published_date())
    print("Book 5 Category:", book5.get_category())
    book1.set_book_name("Advanced Python Programming")
    print("Updated Book 1 Name:", book1.get_book_name())