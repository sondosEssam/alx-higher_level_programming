#!/usr/bin/python3
"""
0-square.py omdule
"""


class Square:
    """
    spuare class documination
    attributes:
    __size: provte size value
    __position: position tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ constructor
        args:
        size: size of the square
        """
        self.size = size
        self.position = position

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
            [print() for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                print(" " * self.__position[0], end="")
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

    @property
    def position(self):
        """Getter for posiotn
        Returns:
        tuple(int): position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        setter for postion
        args:
        value: value of the tuple
        """
        if (not isinstance(value, tuple) or len(value) != 2) or \
            not all(isinstance(i, int) for i in value) or \
                not all(i > 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
