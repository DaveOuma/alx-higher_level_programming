#!/usr/bin/python3
"""
Raise Name Exception with Message
"""

def raise_exception_msg(message=""):
    """
    Raises a name exception with a given message.

    Args:
        message (str): The message to include in the exception.

    Raises:
        NameError: Always raises a name exception with the provided message.
    """
    raise NameError(message)
