#!/usr/bin/python3
def uppercase(str):
    if len(str) == 0:
        print("{}".format(""))
    for i in range(0, len(str)):
        j = str[i]
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            j = chr(ord(str[i]) - 32)
        print("{}".format(j), end="" if (i != len(str) - 1) else "\n")
