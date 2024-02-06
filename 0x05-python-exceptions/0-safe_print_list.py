#!/usr/bin/python3
"""
Safe List Printing
"""

def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    Args:
        my_list (list): The input list.
        x (int): Number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    try:
        printed_count = 0
        for i in range(x):
            print(my_list[i], end="")
            printed_count += 1
        print()
        return printed_count
    except IndexError:
        print()
        return printed_count

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
