#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_mat = []
    for i in matrix:
        new_listi = []
        for j in i:
            new_listi.append(j ** 2)
        new_mat.append(new_listi)
    return new_mat
