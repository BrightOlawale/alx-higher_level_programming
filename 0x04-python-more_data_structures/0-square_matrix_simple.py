#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    out_matrix = []
    for row in matrix:
        in_matrix = []
        for elem in row:
            in_matrix.append(elem**2)
        out_matrix.append(in_matrix)
    return out_matrix
