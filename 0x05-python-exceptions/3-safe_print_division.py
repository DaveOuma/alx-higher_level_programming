#!/usr/bin/python3
"""
Integers Division with Debug
"""

def safe_print_division(a, b):
    """
    Divide two integers and print the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The result of the division, or None if an exception occurs.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
