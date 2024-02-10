#!/usr/bin/python3
""" Module: 5-square """


class Square:
    """ Defines a square """

    def __init__(self, size=0):
        """ Initializes the Square instance with a size """
        self.size = size

    @property
    def size(self):
        """ Getter method for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Computes the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square using '#' """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

