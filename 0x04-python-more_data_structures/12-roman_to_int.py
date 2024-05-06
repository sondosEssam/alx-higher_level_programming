#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return
    num = 0
    curr = 0
    prev = 0
    ch = 0
    for i in range(len(roman_string) - 1, 0, -1):
        curr = romans[roman_string[i]]
        prev = romans[roman_string[i - 1]]
        if ch == 0:
            num += curr
            if curr > prev:
                ch = 1
                continue
        if ch == 1:
            num -= curr
    if (ch == 0):
        num += romans[roman_string[0]]
    else:
        num -= romans[roman_string[0]]
    return num
