#!/usr/bin/python3

"""
This script contains functions related to object introspection and inheritance in Python.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)

class BaseClass:
    """This is a superclass, baseclass, or parentclass."""
    def __init__(self):
        pass

    def example_method(self):
        """An example method."""
        pass

class SubClass(BaseClass):
    """This is a subclass."""
    def __init__(self):
        super().__init__()

    def new_method(self):
        """A new method specific to the subclass."""
        pass

def main():
    """Main function to demonstrate usage."""
    obj = SubClass()
    print("Attributes and methods of SubClass:")
    print(lookup(obj))

    print("\nAttributes and methods of BaseClass:")
    print(lookup(BaseClass))

    print("\nAttributes and methods of int class:")
    print(lookup(int))

if __name__ == "__main__":
    main()

