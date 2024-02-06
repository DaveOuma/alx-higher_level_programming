#!/usr/bin/python3
"""
Safe Integer Print with Error Message
"""

def safe_print_integer_err(value):
    """
    Print an integer with "{:d}".format() and handle errors.

    Args:
        value: The input value.

    Returns:
        bool: True if the value has been correctly printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
