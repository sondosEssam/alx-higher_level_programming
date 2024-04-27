#!/usr/bin/python3
"""
rectangle module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str when priting square instance
        """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - " + \
            f"{self.__width}"

    @property
    def size(self):
        """
        square size
        """
        return self.__height

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value
        self.__width  = value

    def update(self, *args, **kwargs):
        """
        update attrivbutes
        """
        if len(args) == 0:
            if len(kwargs) == 0:
                return
            for attr, value in kwargs.items():
                setattr(self, attr, value)
        argsnames = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, argsnames[i], args[i])
