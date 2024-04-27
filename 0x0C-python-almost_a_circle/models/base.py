#!/usr/bin/python3
"""
base modules for all other modules
"""


class Base:
    """
    base class for all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        d
        """
        if list_dictionaries is None:
            return "[]"
        else:
            import json
            return json.dumps(list_dictionaries)
