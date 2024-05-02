#!/usr/bin/python3
"""
documination
"""


def pascal_triangle(n):
    """
    studnet
    """
    m = [[1]]
    if n <= 0:
        return []
    i = 0
    indforprev = 0
    while n > 1:
        prevlist = m[i]
        newlist = [1]
        for q in range(0, len(prevlist) - 1):
            newlist.append(prevlist[q] + prevlist[q + 1])
        newlist.append(1)
        i += 1
        m.append(newlist)
        n -= 1
    return m
