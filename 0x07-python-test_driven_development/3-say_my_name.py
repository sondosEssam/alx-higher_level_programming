#!/usr/bin/python3
"""
0-add_integer.py
"""


def say_my_name(first_name, last_name=""):
    """
    matrix_devided
    args:
    first_name(int): 1st no
    last_name(int): second no
    Returns:
    int
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if first_name is None:
        first_name = ""
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name is None:
        last_name = ""
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
