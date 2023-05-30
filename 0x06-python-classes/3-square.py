#!/usr/bin/python3
"""Square module
It contains a class that defines a square and init method that
sets its size and schecking if the given values are right. There's also an
area method that returns the area  of the square
"""


class Square():
    """Defines a square"""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one side of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
