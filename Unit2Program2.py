class Library:

    # Constructor to initialize book details
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    # Method to check out a book
    def checkout(self):
        if self.available:
            self.available = False
            print(self.book_name, "has been checked out.")
        else:
            print(self.book_name, "is not available.")

    # Method to return a book
    def return_book(self):
        self.available = True
        print(self.book_name, "has been returned.")

    # Method to display book details
    def display(self):
        status = "Available" if self.available else "Not Available"
        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)
        print()


# Creating objects for books
book1 = Library("Python Basics", "John Smith")
book2 = Library("Data Structures", "Mark Lee")

# Display books
book1.display()
book2.display()

# Checkout and return operations
book1.checkout()
book1.display()

book1.return_book()
book1.display()