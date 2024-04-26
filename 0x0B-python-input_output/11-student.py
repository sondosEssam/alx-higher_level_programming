#!/usr/bin/python3
"""
documination
"""


class Student:
    """
    studnet
    """

    def __init__(self, first_name, last_name, age):
        """"
        studnet
        """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """"
        json
        """
        dicti = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if type(i) is str and self.__dict__.get(i) is not None:
                dicti[i] = self.__dict__[i]
        return dicti

    def reload_from_json(self, json):
        """"
        json
        """
        if json is None:
            return
        for i, j in json.items():
            setattr(self, i , j) 
