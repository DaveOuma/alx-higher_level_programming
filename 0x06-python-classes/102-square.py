class Square:
    """
    Defines a square
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with a size
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Defines the equality comparison for two squares based on their areas
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Defines the inequality comparison for two squares based on their areas
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Defines the less-than comparison for two squares based on their areas
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Defines the less-than-or-equal comparison for two squares based on their areas
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Defines the greater-than comparison for two squares based on their areas
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Defines the greater-than-or-equal comparison for two squares based on their areas
        """
        return self.area() >= other.area()
