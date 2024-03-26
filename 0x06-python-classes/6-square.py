#!/usr/bin/python3
""" Module: 6-square """


class Square:
    """  Defines a square  """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the Square instance with a size and position """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter method for size  """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter method for position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method for position """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Computes the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square using '#' """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
