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

    def to_json(self):
        """"
        json
        """
        return self.__dict__
