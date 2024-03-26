#!/usr/bin/python3
"""
Module: 2-square
"""


class Square:
    """
    Defines a square
    """
    def __init__(self, size=0):
        """
        Initializes the Square instance with a size
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
