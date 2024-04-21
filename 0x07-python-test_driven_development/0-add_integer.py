#!/usr/bin/python3
"""
0-add_integer.py
"""


def add_integer(a, b=98):
    """
    add_integer
    args:
    a(int): 1st no
    b(int): second no
    Returns:
    int
    """
    if not type(a) in (float, int):
        raise TypeError("a must be an integer")
    elif not type(b) in (float, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
