#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = list(tuple_a)
    list2 = list(tuple_b)
    if len(list1) == 0:
        list1.append(0)
    if len(list1) == 1:
        list1.append(0)
    if len(list2) == 0:
        list2.append(0)
    if len(list2) == 1:
        list2.append(0)
    return (list1[0] + list2[0] , list1[1] + list2[1])
