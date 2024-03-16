#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    listi = []
    for listi in matrix:
        if listi == []:
            print()
        for i in range(0, len(listi)):
            print("{:d}".format(listi[i]), end=" " if listi[i] != listi[-1] else "\n")
