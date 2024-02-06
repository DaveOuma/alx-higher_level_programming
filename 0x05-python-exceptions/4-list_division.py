#!/usr/bin/python3
"""
Element-wise List Division
"""

def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element two lists.

    Args:
        my_list_1 (list): The first input list.
        my_list_2 (list): The second input list.
        list_length (int): The desired length of the resulting list.

    Returns:
        list: A new list with all divisions.
    """
    result = []
    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except (TypeError, ValueError):
            print("wrong type")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result.append(division_result)

    return result
