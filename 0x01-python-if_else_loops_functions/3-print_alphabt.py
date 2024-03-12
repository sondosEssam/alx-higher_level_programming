#!/usr/bin/python3
import random
for i in range(97, 123):
    j = chr(i)
    print("{}".format(j), end="") if j != 'q' and j != 'e' else ""
