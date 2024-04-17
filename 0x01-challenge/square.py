#!/usr/bin/python3

"""This module defines a Square class."""


class Square:
    """Defines the Square class."""

    def __init__(self, size):
        """Initializes the Square instance."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area_of_my_square(self):
        """Area of the square"""
        return self.__size * self.__size

    def permiter_of_my_square(self):
        """Returns the perimeter of the square."""
        return self.__size * 4

    def __str__(self):
        """Returns a string representation of the square."""
        return f"{self.size}/{self.size}"


if __name__ == "__main__":

    s = Square(size=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
