#!/usr/bin/python3
"""
1-mylist module
"""


def inherits_from(obj, a_class):
    """
    MyList
    """
    if isinstance(obj, a_class) is True and type(obj) is not a_class:
        return True
    return False
