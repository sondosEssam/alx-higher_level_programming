#!/usr/bin/python3
""""
0-read_file v.3
"""


def class_to_json(obj):
    """"
    read file
    """
    if not hasattr(obj, "__dict__"):
        return
    return obj.__dict__
