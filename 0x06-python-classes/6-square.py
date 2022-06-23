#!/usr/bin/python3
""" Creates a class called Square which is empty
"""


class Square:
    """ Empty class with private attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """
                Instantiation with size
        Args:
            size: Size of the square
            position: Postion of the square
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        size getter. Handle size errors
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter. Set the size of the square
        """
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Print a square with the character # at the position given
        """
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """
        position setter. Set the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Handle position with errors
        """
        if type(value) != tuple:
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is False:
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is False:
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("Position must be a tuple of 2 positive integers")
        else:
            self.__position = value
