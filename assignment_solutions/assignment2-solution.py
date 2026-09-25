def validate_invoice(line):
    """
    Validates a single invoice line.
    
    Returns:
        float: The valid invoice amount if all checks pass.
        None: If the record is invalid or corrupted.
    """
    cleaned_line = line.strip()
    fields = cleaned_line.split(",")

    # Check for exactly 3 comma-separated fields
    if len(fields) != 3:
        return None

    invoice_id, customer_name, amount_str = fields

    # Check if Customer Name is missing or empty
    if not customer_name.strip():
        return None

    # Try converting Amount to float and ensure it is > 0
    try:
        amount = float(amount_str)
        if amount <= 0:
            return None
        return amount
    except ValueError:
        return None


def main():
    total_valid_count = 0
    total_skipped_count = 0
    total_valid_revenue = 0.0

    # Read and process invoices.txt
    with open("invoices.txt", "r") as file:
        for line in file:
            # Skip empty lines in the text file
            if not line.strip():
                continue

            amount = validate_invoice(line)

            if amount is not None:
                total_valid_count += 1
                total_valid_revenue += amount
            else:
                total_skipped_count += 1

    # Write output to summary_report.txt
    with open("summary_report.txt", "w") as report:
        report.write("--- Invoice Processing Summary ---\n")
        report.write(f"Total Valid Invoices: {total_valid_count}\n")
        report.write(f"Total Skipped Records: {total_skipped_count}\n")
        report.write(f"Total Valid Revenue: ${total_valid_revenue:.2f}\n")


if __name__ == "__main__":
    main()