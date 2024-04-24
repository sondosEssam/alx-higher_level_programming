#!/usr/bin/python3
"""
1-mylist module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    rectangle
    """
    def __init__(self, width, height):
        """
        __init__
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
