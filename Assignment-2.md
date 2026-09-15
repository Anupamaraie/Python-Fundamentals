# 📄 Mid-Course Project: Invoice Data Cleaner & Summarizer

## 📌 Project Overview
In real software systems, data entered by humans or external systems often contains errors. If a program encounters a bad line of data, it shouldn't crash—it should skip the bad line, report the error, and keep processing the rest of the file.

In this project, you will write a Python program that reads raw invoice records from a text file, filters out corrupted data, calculates total valid revenue, and saves a summary report to a new file.

---

## 🎯 Concepts Covered
- **Functions:** Packaging reusable logic with parameters and `return` statements.
- **File I/O:** Reading files with `open()` and writing output text files.
- **String Operations:** Cleaning text with `.strip()` and splitting text with `.split()`.
- **Control Flow & Error Handling:** `for` loops, `if/else` checks, and `try/except` blocks.

---

## 🛠️ Data Format & Rules

### Input File Format (`invoices.txt`)
Each line in your input file represents one invoice record:
`InvoiceID,CustomerName,Amount`

**Example Input Data (`invoices.txt`):**

```
INV-101,Acme Corp,1500.50
INV-102,Beta LLC,500.00
INV-103,Gamma Inc,-200.00
INV-104,,850.00
INV-105,Delta Co,abc

```

## 🛠️ Data Validation Rules

A record is considered **invalid** and should be skipped if:
1. It does not contain **exactly 3 values** separated by commas.
2. The **Customer Name** is missing or empty.
3. The **Amount** is not a valid number.
4. The **Amount** is zero or negative ($\le 0$).

---

## 🚀 Step-by-Step Instructions

### Step 1: Set Up Project Files
Create a project folder structured like this:

```text
invoice-cleaner/
├── invoices.txt
├── main.py
├── summary_report.txt
└── README.md

```

## Step 2: Write the Line Validation Function

### Write a function validate_invoice(line) that:
  Removes extra spaces around the string using .strip().
  Splits the line into a list using .split(",").
  Checks if all 3 fields exist and verifies that the customer name is not empty.
  Converts the amount to a float and ensures it is greater than 0.

Returns: The valid amount as a float if everything is correct, or None if the line is invalid.

## Step 3: Read and Process the File
In your main script (main.py):
  Open invoices.txt and iterate through it line-by-line using a for loop.
  Use a try/except block to catch any float conversion errors gracefully.
  Keep track of the following variables:
  Total count of valid invoices
  Total count of skipped (corrupted) records
  Total sum of valid invoice amounts

## Step 4: Write the Output Summary Report
### Write the final metrics into summary_report.txt using file writing mode: open("summary_report.txt", "w").
