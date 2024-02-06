#!/usr/bin/python3
"""
Safe Printing of List Integers
"""

def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list containing only integers.

    Args:
        my_list (list): The input list.
        x (int): Number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """
    integer_count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                integer_count += 1
        print()
    except IndexError:
        pass
    return integer_count
