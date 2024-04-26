#!/usr/bin/python3
"""
0-read_file v.3
"""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item():
  """
  fun to add items
  """
  filename = "add_item.json"
  with open(filename, mode="w", encoding="UTF8") as f:
    arg = sys.argv[1:]
    r = load_from_json_file(sys.argv[0])
    for i in arg:
        r.append(i)
  save_to_json_file(r, filename)

add_item()
