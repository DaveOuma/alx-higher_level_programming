#!/usr/bin/python3
from raise_exception_msg import raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
