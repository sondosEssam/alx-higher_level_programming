#!/usr/bin/python3
""""
0-read_file v.3
"""


def load_from_json_file(filename):
    """"
    read file
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        import json
        return json.load(f)
