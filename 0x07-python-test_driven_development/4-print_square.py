#!/usr/bin/python3
"""
0-add_integer.py
"""


def print_square(size):
    """
    matrix_devided
    args:
    matrix(int): 1st no
    div(int): second no
    Returns:
    int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
