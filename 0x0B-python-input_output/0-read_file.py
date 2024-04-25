#!/usr/bin/python3
""""
0-read_file v.3
"""


def read_file(filename=""):
    """"
    read file
    """
    with open(filename, encoding="UTF8") as f:
        line = f.read()
        print(line, end="")
