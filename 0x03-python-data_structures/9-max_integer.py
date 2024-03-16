#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    a = -1
    for i in my_list:
        if a < i:
            a = i
    return a
