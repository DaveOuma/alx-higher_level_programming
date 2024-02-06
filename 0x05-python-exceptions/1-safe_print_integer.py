#!/usr/bin/python3
"""
Safe Integer Printing
"""

def safe_print_integer(value):
    """
    Print an integer with "{:d}".format().

    Args:
        value: The input value.

    Returns:
        bool: True if the value has been correctly printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

# Example usage:
if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
