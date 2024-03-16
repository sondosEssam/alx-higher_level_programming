#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    listi = []
    for listi in matrix:
        #print(listi)
        for i in listi:
            print("{}".format(i),end=" " if i != listi[-1] else "\n")
