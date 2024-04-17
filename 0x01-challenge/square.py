#!/usr/bin/python3

"""This module defines a Square class."""


class Square:
    """Defines the Square class."""

    def __init__(self, width, height):
        """Initializes the Square instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the square."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the square."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the square."""
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area_of_my_square(self):
        """Area of the square"""
        return self.__width * self.__height

    def permiter_of_my_square(self):
        """Returns the perimeter of the square."""
        return self.__width * 4

    def __str__(self):
        """Returns a string representation of the square."""
        return f"{self.width}/{self.height}"


if __name__ == "__main__":

    s = Square(width=5, height=5)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
