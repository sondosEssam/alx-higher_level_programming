#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return my_list
    my_list[idx], element = element, my_list[idx]
    return my_list
