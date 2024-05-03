#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_listi = set(my_list)
    if not my_list:
        return 0
    i = 0
    for j in new_listi:
        i += j
    return i
