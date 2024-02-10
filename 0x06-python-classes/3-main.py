#!/usr/bin/python3
""" 3-main """
Square = __import__('3-square').Square

try:
    my_square_1 = Square(3)
    print(f"Area: {my_square_1.area()}")
except Exception as e:
    print(e)

try:
    print(f"{my_square_1.size}")
except Exception as e:
    print(e)

try:
    print(f"{my_square_1.__size}")
except Exception as e:
    print(e)

my_square_2 = Square(5)
print(f"Area: {my_square_2.area()}")

