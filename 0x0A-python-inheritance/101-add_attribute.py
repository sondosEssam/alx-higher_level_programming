#!/usr/bin/python3
"""
1-mylist module
"""


def add_attribute(cls, attr, val):
    """
    MyList
    """
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, attr, val)
