#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            j = chr(ord(str[i]) - 32)
            print(j, end="" if (i != len(str) - 1) else "\n")
        else:
            print(str[i], end="" if (i != len(str) - 1) else "\n")
