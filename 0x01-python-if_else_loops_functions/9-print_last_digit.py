#!/usr/bin/python3
def print_last_digit(number):
    s = str((number))
    r = (int(s[-1]))
    print("{}".format(r), end="")
    return r
