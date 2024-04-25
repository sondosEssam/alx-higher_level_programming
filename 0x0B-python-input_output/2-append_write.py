#!/usr/bin/python3
""""
0-read_file v.3
"""


def append_write(filename="", text=""):
    """"
    read file
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        f.append(text)
    return len(text)
