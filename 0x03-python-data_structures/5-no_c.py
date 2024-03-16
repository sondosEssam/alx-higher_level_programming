#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    listi = []
    for i in range(0, len(my_string)):
        if my_string[i] != 'c'and my_string[i] != 'C':
            listi.append(my_string[i])
    return ''.join(listi)
