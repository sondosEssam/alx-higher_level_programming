#!/usr/bin/python3
""""
0-read_file
"""


def read_file(filename=""):
    """"
    read file
    """
    with open(filename, encoding="UTF8") as f:
        line = f.read()
        print(line, end="")
