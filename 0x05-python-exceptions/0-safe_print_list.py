#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        for i in my_list:
            print(i, end="")
            j += 1
        print()
        return j
    except IndexError as e:
        print()
