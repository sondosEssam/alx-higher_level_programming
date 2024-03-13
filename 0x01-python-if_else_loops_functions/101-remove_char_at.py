#!/usr/bin/python3
def remove_char_at(str, n):
    listi = []
    for i in range(0, len(str)):
        if i != n:
            listi.append(str[i])
    return ''.join(listi)
