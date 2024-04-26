#!/usr/bin/python3
"""
7-add_item.py

This script reads command-line arguments, appends them to a list in memory,
and then saves the updated list to a JSON file named "add_item.json".

It assumes the existence of two other Python files:

- 5-save_to_json_file.py: This file should contain a function named
  `save_to_json_file` that takes a list and a filename as arguments and
  saves the list to a JSON file.

- 6-load_from_json_file.py: This file should contain a function named
  `load_from_json_file` that takes a filename as an argument and loads a
  list from the corresponding JSON file.
"""

import sys
"""
save json file
"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
"""
load json file
"""
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
""""
additional one
"""

filename = "add_item.json"
with open(filename, mode="a", encoding="UTF8") as f:
    arg = sys.argv[1:]
    remin = load_from_json_file(filename)
    for i in arg:
        remin.append(i)
    save_to_json_file(remin, filename)
