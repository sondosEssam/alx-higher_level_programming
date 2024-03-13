#!/usr/bin/python3
i = 122
flag = True
while i >= 97:
    j = chr(i)
    print("{}".format(j) if flag is True else "{}".format(chr(i - 32)), end="")
    if flag is True:
        flag = False
    else:
        flag = True
    i = i - 1
