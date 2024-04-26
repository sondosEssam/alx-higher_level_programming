#!/usr/bin/python3
""""
0-read_file v.3
"""

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
with open(filename, mode="a", encoding="UTF8") as f:
    arg = sys.argv[1:]
    remin = load_from_json_file(filename)
    for i in arg:
        remin.append(i)
    save_to_json_file(remin, filename)
