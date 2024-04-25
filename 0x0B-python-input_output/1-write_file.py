#!/usr/bin/python3
""""
0-read_file v.3
"""


def write_file(filename="", text=""):
    """"
    read file
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        f.write(text)
