#!/usr/bin/python3
"""
0-square.py omdule
"""


class Square:
    """
    spuare class documination
    attributes:
    __size: provte size value
    """
    def __init__(self, size=0):
        """ __init__ constructor
        args:
        size: size of the square
        """
        self.size = size

    def area(self):
        """
        area: area of the square
        Returns:
        float: area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        my_print
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """Getter for the size property.
        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size property.
        Args:
            value (int): The new value for the size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
