# 📌 Minor Assignment 2: Simple Library Catalog

## **Overview**
Build a simple Python application to manage a library catalog. This project will help you combine **Object-Oriented Programming (OOP)**, **JSON file storage**, **list comprehensions**, and **lambda functions** into one working system.

---

## **Learning Objectives**
By completing this assignment, you will practice:
1. Creating basic Python classes and working with object attributes/methods.
2. Saving and loading data using **JSON** files so your data isn't lost when the program closes.
3. Writing clean, efficient code using **list comprehensions**.
4. Using **lambda functions** for searching and sorting data.

---

## **Step-by-Step Instructions**

### **Step 1: Create the `Book` Class**
Define a `Book` class to represent a single book in the library.

* **Attributes:**
  * `book_id` (int): Unique identifier for the book.
  * `title` (str): Title of the book.
  * `author` (str): Author's name.
  * `genre` (str): Genre/category of the book.
  * `is_checked_out` (bool): `True` if checked out, `False` if available (default: `False`).

* **Methods:**
  * `check_out()`: Changes `is_checked_out` to `True` if it is available.
  * `return_book()`: Changes `is_checked_out` to `False`.
  * `display()`: Prints the details of the book in a readable format.

---

### **Step 2: Save and Load Data (JSON)**
To make sure your library keeps its books saved on your computer, use Python's built-in `json` module.

* **Loading:** At the start of the program, read data from `library.json` and convert each dictionary entry into a `Book` object in a list.
* **Saving:** Whenever a new book is added or a book's status changes, save the current list of books back to `library.json`.

---

### **Step 3: Practice List Comprehensions**
Use **list comprehensions** in your program for quick operations:

1. **Available Books:** Get a list of all books that are currently available:
   ```python
   available_books = [b for b in books if not b.is_checked_out]
   ```
2. **Convert Objects to Dictionaries:** Prepare books for saving to JSON:
   ```python
   book_data = [{"book_id": b.book_id, "title": b.title, "author": b.author, "genre": b.genre, "is_checked_out": b.is_checked_out} for b in books]
   ```

---

### **Step 4: Practice Lambda Functions**
Use **lambda functions** for searching and sorting:

1. **Search Books:** Use `filter()` with a `lambda` to search for a keyword in titles or authors:
   ```python
   search_results = list(filter(lambda b: query in b.title.lower() or query in b.author.lower(), books))
   ```
2. **Sort Books:** Use `sorted()` with a `lambda` to display books alphabetically by title:
   ```python
   sorted_books = sorted(books, key=lambda b: b.title.lower())
   ```

---

### **Step 5: Build a Simple Menu (CLI)**
Create a `while` loop that gives users options to interact with the catalog:

```
=== 📚 Simple Library Catalog ===
1. View All Books
2. Search for a Book
3. View Available Books
4. Add a New Book
5. Check Out a Book
6. Return a Book
7. Exit
```

---

## **Resume Tip 💡**
When adding this project to your resume or portfolio, highlight the technical concepts you used:

* **Project Title:** Command-Line Library Management System
* **Key Skills:** Python, OOP, JSON Data Handling, Functional Programming (Lambdas, Comprehensions)
* **Bullet Point:** Designed an interactive CLI application utilizing Object-Oriented principles, JSON data persistence, and Pythonic functional paradigms to handle catalog queries and state management.
