#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    my = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return my
    my[idx] = element
    return my_list
