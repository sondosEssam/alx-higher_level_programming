#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my = my_list.copy()
    if len(my_list) == 0 or idx < 0:
        return my
    my_list[idx], element = element, my_list[idx]
    return my_list
