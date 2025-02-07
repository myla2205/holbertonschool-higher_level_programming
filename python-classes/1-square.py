#!/usr/bin/python3
"""Define a class named Square."""


class Square:
    """This class represents a Square."""

    def __init__(self, size=0):
        """Instantiation with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # set both width and height

    @property
    def size(self):
        """Function to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Function to set the size of the square.

        Args:
            value (int): must be an int.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        self.__width = value  # Set width to the size value
        self.__height = value  # Set height to the size value

    @property
    def width(self):
        """Function to retrieve the width of the square."""
        return self.__width

    @property
    def height(self):
        """Function to retrieve the height of the square."""
        return self.__height
