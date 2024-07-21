class Book:
  """
  Base class representing a book with title and author.
  """
  def __init__(self, title, author):
    """
    Initializes a Book instance with title and author.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    self.title = title
    self.author = author

class EBook(Book):
  """
  Derived class representing an Ebook with additional file size attribute.
  """
  def __init__(self, title, author, file_size):
    """
    Initializes an EBook instance with title, author, and file size.

    Args:
        title (str): The title of the Ebook.
        author (str): The author of the Ebook.
        file_size (int): The file size of the Ebook in KB.
    """
    super().__init__(title, author)  # Call base class constructor
    self.file_size = file_size

class PrintBook(Book):
  """
  Derived class representing a PrintBook with additional page count attribute.
  """
  def __init__(self, title, author, page_count):
    """
    Initializes a PrintBook instance with title, author, and page count.

    Args:
        title (str): The title of the PrintBook.
        author (str): The author of the PrintBook.
        page_count (int): The page count of the PrintBook.
    """
    super().__init__(title, author)  # Call base class constructor
    self.page_count = page_count

class Library:
  """
  Class representing a library that manages a collection of books.
  """
  def __init__(self):
    """
    Initializes a Library instance with an empty list of books.
    """
    self.books = []

  def add_book(self, book):
    """
    Adds a Book, EBook, or PrintBook instance to the library collection.

    Args:
        book (Book, EBook, or PrintBook): The book object to be added.
    """
    if isinstance(book, Book):  # Check if book is a valid subclass of Book
      self.books.append(book)
    else:
      print("Invalid book type. Please add a Book, EBook, or PrintBook object.")

  def list_books(self):
    """
    Prints details of all books in the library.
    """
    for book in self.books:
      if isinstance(book, EBook):
        print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
      elif isinstance(book, PrintBook):
        print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
      else:
        print(f"Book: {book.title} by {book.author}")

from library_system import Book, EBook, PrintBook, Library

def main():
  # Create a Library instance
  my_library = Library()

  # Create instances of each type of book
  classic_book = Book("Pride and Prejudice", "Jane Austen")
  digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
  paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

  # Add books to the library
  my_library.add_book(classic_book)
  my_library.add_book(digital_novel)
  my_library.add_book(paper_novel)

  # List all books in the library
  my_library.list_books()

if __name__ == "__main__":
  main()
