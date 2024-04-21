#!/usr/bin/python3
"""
0-add_integer.py
"""


def text_indentation(text):
    """
    matrix_devided
    args:
    matrix(int): 1st no
    div(int): second no
    Returns:
    int
    """
    if not isinstance(text, str):
        raise TypeError("stext must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?':
            print()
            print()
            while i + 1 < len(text) and (text[i + 1] == ' ' or text[i - 1] == ' '):
                i += 1
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
