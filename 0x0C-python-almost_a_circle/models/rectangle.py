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

    def __str__(self):
        """
        str when priting rectangl instance
        """
        return f"({self.id}) {self.__x}/{self.__y} - " + \
            f"{self.__width}/{self.__height}"

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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area = width * height
        """
        return self.__width * self.__height

    def display(self):
        """
        display #
        """
        for _ in range(self.__height):
            print("#" * self.__width + "\n", end="")
