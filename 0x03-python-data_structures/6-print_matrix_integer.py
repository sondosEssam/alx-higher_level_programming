#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    listi = []
    for listi in matrix:
        if listi == []:
            print()
        for i in listi:
            print("{}".format(i),end=" " if i != listi[-1] else "\n")
