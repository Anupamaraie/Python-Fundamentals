# ==============================================================================
# 📌 MINOR ASSIGNMENT 2: SIMPLE LIBRARY CATALOG (BEGINNER SOLUTION)
# Concepts Covered: OOP Classes, JSON Storage, List Comprehensions, Lambda Functions
# ==============================================================================

import json

# ------------------------------------------------------------------------------
# STEP 1: DEFINE THE BOOK CLASS
# ------------------------------------------------------------------------------
class Book:
    """Represents a single book in the library catalog."""

    def __init__(self, book_id, title, author, genre, is_checked_out=False):
        # Store basic properties of the book
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = is_checked_out

    def check_out(self):
        """Mark the book as checked out if it is currently available."""
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned to the library."""
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def to_dict(self):
        """Convert object data into a standard dictionary for easy JSON saving."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "is_checked_out": self.is_checked_out
        }


# ------------------------------------------------------------------------------
# STEP 2 & 3: FILE PERSISTENCE & DATA MANAGEMENT FUNCTIONS
# ------------------------------------------------------------------------------
FILENAME = "library.json"

def load_books():
    """Reads library.json and returns a list of Book objects."""
    try:
        with open(FILENAME, "r") as file:
            raw_data = json.load(file)
            
            # Beginner List Comprehension: Convert dict items to Book objects
            books = [
                Book(
                    item["book_id"],
                    item["title"],
                    item["author"],
                    item["genre"],
                    item["is_checked_out"]
                )
                for item in raw_data
            ]
            return books
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty list if file doesn't exist or is invalid
        return []


def save_books(books):
    """Saves the current list of Book objects into library.json."""
    with open(FILENAME, "w") as file:
        # Beginner List Comprehension: Convert Book objects to dictionaries
        book_dicts = [b.to_dict() for b in books]
        json.dump(book_dicts, file, indent=4)


# ------------------------------------------------------------------------------
# STEP 4: LAMBDA FUNCTIONS & LIST COMPREHENSIONS FOR SEARCH/SORT
# ------------------------------------------------------------------------------

def get_available_books(books):
    """List comprehension to filter only available books."""
    return [b for b in books if not b.is_checked_out]


def search_books(books, query):
    """Lambda function combined with filter() to match search query."""
    q = query.lower()
    # Lambda checks if query exists in book title OR author name
    search_filter = lambda b: q in b.title.lower() or q in b.author.lower()
    return list(filter(search_filter, books))


def sort_books_by_title(books):
    """Lambda function used as a key for sorting books alphabetically."""
    return sorted(books, key=lambda b: b.title.lower())


# ------------------------------------------------------------------------------
# STEP 5: INTERACTIVE CLI MENU
# ------------------------------------------------------------------------------
def main():
    books = load_books()

    while True:
        print("\n=== 📚 Simple Library Catalog ===")
        print("1. View All Books (Sorted by Title)")
        print("2. Search for a Book")
        print("3. View Available Books Only")
        print("4. Add a New Book")
        print("5. Check Out a Book")
        print("6. Return a Book")
        print("7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "1":
            sorted_list = sort_books_by_title(books)
            print("\n--- All Books in Library ---")
            if not sorted_list:
                print("No books in catalog yet.")
            for b in sorted_list:
                status = "❌ Checked Out" if b.is_checked_out else "✅ Available"
                print(f"[{b.book_id}] '{b.title}' by {b.author} | Genre: {b.genre} | {status}")

        elif choice == "2":
            query = input("Enter title or author keyword: ")
            results = search_books(books, query)
            print(f"\n--- Search Results ({len(results)} found) ---")
            for b in results:
                status = "❌ Checked Out" if b.is_checked_out else "✅ Available"
                print(f"[{b.book_id}] '{b.title}' by {b.author} | {status}")

        elif choice == "3":
            available = get_available_books(books)
            print(f"\n--- Available Books ({len(available)}) ---")
            for b in available:
                print(f"[{b.book_id}] '{b.title}' by {b.author}")

        elif choice == "4":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            genre = input("Genre: ").strip()
            
            # Generate a simple auto-incrementing ID
            new_id = 1 if not books else max([b.book_id for b in books]) + 1
            new_book = Book(new_id, title, author, genre)
            books.append(new_book)
            save_books(books)
            print(f"✅ Book '{title}' added successfully!")

        elif choice == "5":
            book_id = int(input("Enter Book ID to check out: "))
            found = False
            for b in books:
                if b.book_id == book_id:
                    found = True
                    if b.check_out():
                        save_books(books)
                        print(f"✅ You checked out '{b.title}'!")
                    else:
                        print("❌ Sorry, this book is already checked out.")
                    break
            if not found:
                print("❌ Book ID not found.")

        elif choice == "6":
            book_id = int(input("Enter Book ID to return: "))
            found = False
            for b in books:
                if b.book_id == book_id:
                    found = True
                    if b.return_book():
                        save_books(books)
                        print(f"✅ Thank you! '{b.title}' is returned.")
                    else:
                        print("❌ This book was not checked out.")
                    break
            if not found:
                print("❌ Book ID not found.")

        elif choice == "7":
            print("Goodbye! Data saved.")
            break


if __name__ == "__main__":
    main()