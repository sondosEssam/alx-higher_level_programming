#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    num = 0
    curr = 0
    ch = romans[roman_string[len(roman_string) - 1]]

    i = 0
    while i < len(roman_string):
        curr = romans[roman_string[i]]
        num += curr
        i += 1
    i = len(roman_string) - 2
    while i >= 0:
        curr = romans[roman_string[i]]
        if curr < ch:
            num -= (2 * curr)
        i -= 1
    return num
