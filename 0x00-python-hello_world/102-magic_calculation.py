#!/usr/bin/python3
import dis
def myfunc(a, b):
    return 98 + a ** b
dis.dis(myfunc)
