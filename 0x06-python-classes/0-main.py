#!/usr/bin/python3
"""0-main for testing the representation for 0-square.py"""

Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
