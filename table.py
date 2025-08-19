#This is created by AI agent kickStart by Danish Akhtar
def print_table(data):
    """Prints a formatted table from a list of dictionaries.

    Args:
        data: A list of dictionaries, where each dictionary represents a row
              in the table.  All dictionaries must have the same keys.
    """
    if not data:
        print("No data to display.")
        return

    # Extract headers from the first row
    headers = list(data[0].keys())
    
    # Calculate column widths
    col_widths = [max(len(str(row[header])) for row in data) + 2 for header in headers]

    # Print header row
    header_row = "|".join(header.center(width) for header, width in zip(headers, col_widths))
    print("+" + "+" .join("-" * width for width in col_widths) + "+")
    print(header_row)
    print("+" + "+" .join("-" * width for width in col_widths) + "+")


    # Print data rows
    for row in data:
        row_data = [str(row[header]).center(width) for header, width in zip(headers, col_widths)]
        print("|".join(row_data))

    print("+" + "+" .join("-" * width for width in col_widths) + "+")


# Sample usage
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"},
]

print_table(data)

