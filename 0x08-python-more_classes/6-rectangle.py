#!/usr/bin/python3
"""
0-rectangl.py module

"""


class Rectangle:
    """
    rectangle class
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        __init method
        args:
        width: width
        height: this is a height property with the getter and the setter
        """
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """
        getter of the width property
        """
        return self.__width

    @property
    def height(self):
        """
        getter of the heigh property
        """
        return self.__height

    @width.setter
    def width(self, value):
        """"
        setter for the width property
        args:
        value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """"
        setter for the width property
        args:
        value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """ str method to change output when printing the rectangle"""
        string_representation = ""
        for _ in range(self.__height):
            string_representation += "#" * self.__width + "\n"
        return string_representation.rstrip()

    def __repr__(self):
        """
        __reper__ for the rectalne identifying
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        __del for the rectalne identifying
        """
        print("Bye rectangle...")
        number_of_instances -= 1

    def area(self):
        """
        area of the rectangle
        Returns:
        float
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter of the rectangle
        Returns:
        int or float
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2
