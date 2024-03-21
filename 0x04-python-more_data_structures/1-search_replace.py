#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    new_listi = []
    for j in range(len(my_list)):
        if my_list[j] == search:
            new_listi.append(replace)
        else:
            new_listi.append(my_list[j])
    return new_listi
