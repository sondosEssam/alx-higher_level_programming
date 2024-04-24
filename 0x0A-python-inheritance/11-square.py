#!/usr/bin/python3
"""
1-mylist module
"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """
    rectangle
    """
    def __init__(self, size):
        """
        __init__
        """
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        str method
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """"
        area
        """
        return int(self.__size) * int(self.__size)
