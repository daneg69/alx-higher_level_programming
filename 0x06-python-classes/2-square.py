#!/usr/bin/python3
""" Creates a class called Square which is empty
"""


class Square:
    """ Empty class with private attribute
    """
    def __init__(self, size=0):
        """
                Instantiation with size
        Args:
            size: Size of the square
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
