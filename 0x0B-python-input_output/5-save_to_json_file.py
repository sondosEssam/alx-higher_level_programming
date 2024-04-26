#!/usr/bin/python3
""""
0-read_file v.3
"""


def save_to_json_file(my_obj, filename):
    """"
    read file
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        import json
        json.dump(my_obj, f)
