#!/usr/bin/python3
"""
1-mylist module
"""


class BaseGeometry:
    """
    MyList
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    rectangle
    """
    def __init__(self, width, height):
        """
        __init__
        """
        self.__width = super().integer_validator(self, "width", width)
        self.__height = super().integer_validator(self, "height", height)
