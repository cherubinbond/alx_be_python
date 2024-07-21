class Book:
  """
  Represents a book in the library.
  """

  def __init__(self, title, author):
    """
    Initializes a Book object with title, author, and availability status.
    """
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute to track availability

  def check_out(self):
    """
    Marks the book as checked out, changing its availability status.
    """
    self._is_checked_out = True

  def return_book(self):
    """
    Marks the book as returned, making it available again.
    """
    self._is_checked_out = False

  def is_available(self):
    """
    Returns True if the book is available, False otherwise.
    """
    return not self._is_checked_out

class Library:
  """
  Represents a library managing a collection of books.
  """

  def __init__(self):
    """
    Initializes a Library object with an empty list to store books.
    """
    self._books = []

  def add_book(self, book):
    """
    Adds a Book object to the library's collection.
    """
    self._books.append(book)

  def check_out_book(self, title):
    """
    Attempts to check out a book by title, marking it unavailable if found.
    """
    for book in self._books:
      if book.title == title and book.is_available():
        book.check_out()
        print(f"Successfully checked out '{title}'.")
        return
    print(f"Sorry, '{title}' is not available for checkout.")

  def return_book(self, title):
    """
    Attempts to return a book by title, making it available if found.
    """
    for book in self._books:
      if book.title == title:
        book.return_book()
        print(f"Successfully returned '{title}'.")
        return
    print(f"Sorry, '{title}' is not currently checked out.")

  def list_available_books(self):
    """
    Prints information about all available books in the library.
    """
    print("Available books:")
    for book in self._books:
      if book.is_available():
        print(f"{book.title} by {book.author}")
