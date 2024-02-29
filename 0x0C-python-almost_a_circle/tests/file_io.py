#!/usr/bin/python3

def write_to_file(filename, content):
    """Writes content to a file.

    Args:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.
    """
    with open(filename, "w") as file:
        file.write(content)

def read_from_file(filename):
    """Reads content from a file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The content read from the file.
    """
    with open(filename, "r") as file:
        return file.read()

