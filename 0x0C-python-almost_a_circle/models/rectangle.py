#!/usr/bin/python3
"""
rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """
    rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """
        retangle height
        """
        return self.__height

    @property
    def width(self):
        """
        retangle width
        """
        return self.__width

    @property
    def x(self):
        """
        retangle x
        """
        return self.__x

    @property
    def y(self):
        """
        retangle y
        """
        return self.__y

    @height.setter
    def height(self, value):
        """
        height setter
        """
        self.__height = value

    @width.setter
    def width(self, value):
        """
        width setter
        """
        self.__width = value

    @x.setter
    def x(self, value):
        """
        x setter
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """
        y setter
        """
        self.__y = value
