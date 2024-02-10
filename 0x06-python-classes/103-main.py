# Import the MagicClass class
from magic_class import MagicClass

# Create an instance of MagicClass with radius 5
magic_circle = MagicClass(5)

# Test the area method
print("Area of the circle:", magic_circle.area())  # Output should be approximately 78.54

# Test the circumference method
print("Circumference of the circle:", magic_circle.circumference())  # Output should be approximately 31.42

# Change the radius of the circle
magic_circle.radius = 7

# Test the area method again
print("Area of the circle after radius change:", magic_circle.area())  # Output should be approximately 153.94

# Test the circumference method again
print("Circumference of the circle after radius change:", magic_circle.circumference())  # Output should be approximately 43.98

