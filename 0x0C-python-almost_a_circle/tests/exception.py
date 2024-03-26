#!/usr/bin/python3

def divide(x, y):
    """Divides two numbers.

    Args:
        x (int or float): The numerator.
        y (int or float): The denominator.

    Returns:
        float: The result of dividing x by y, or None if y is zero.
    """
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        return result
