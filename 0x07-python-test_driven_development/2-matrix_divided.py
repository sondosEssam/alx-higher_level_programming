#!/usr/bin/python3
"""
0-add_integer.py
"""


def matrix_divided(matrix, div):
    """
    matrix_devided
    args:
    matrix(int): 1st no
    div(int): second no
    Returns:
    int
    """
    new_matrix = []
    row = []
    if not all(type(i) is list for i in matrix) or \
            not matrix or \
            not all(type(j) in (int, float) for i in matrix for j in i):
        raise TypeError("matrix must be a matrix" +
                        " (list of lists) of integers/floats")
    x = len(matrix[0])
    if any(len(i) != x for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not type(div) in (float, int):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            row.append(round(j / div, 2))
        new_matrix.append(row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
