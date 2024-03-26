#!/usr/bin/python3

class Animal:
    """A class representing an animal."""

    def speak(self):
        """Make the animal speak."""
        return "Animal speaks"

class Dog(Animal):
    """A class representing a dog, inheriting from Animal."""

    def speak(self):
        """Make the dog bark."""
        return "Dog barks"

class Cat(Animal):
    """A class representing a cat, inheriting from Animal."""

    def speak(self):
        """Make the cat meow."""
        return "Cat meows"

