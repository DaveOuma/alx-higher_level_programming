class Student:
    """A class representing a student."""

    def __init__(self, name, age):
        """
        Initializes a Student object with the given name and age.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
        """
        self._name = name
        self._age = age

    def get_name(self):
        """
        Gets the name of the student.

        Returns:
            str: The name of the student.
        """
        return self._name

    def set_name(self, name):
        """
        Sets the name of the student.

        Args:
            name (str): The new name of the student.
        """
        self._name = name

    def get_age(self):
        """
        Gets the age of the student.

        Returns:
            int: The age of the student.
        """
        return self._age

    def set_age(self, age):
        """
        Sets the age of the student.

        Args:
            age (int): The new age of the student.
        """
        self._age = age
