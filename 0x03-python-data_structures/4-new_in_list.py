#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return my
    my_list[idx], element = element
    return my_list
