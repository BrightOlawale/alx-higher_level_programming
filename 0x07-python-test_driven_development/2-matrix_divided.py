#!/usr/bin/python3
"""
    Divide a matrix of integers/floats
    by an integer or float
"""


def matrix_divided(matrix, div):
    """
        Function to divide each element of matrix
        by div 
    """
    message_1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(message_1)
    for row in range(len(matrix)):
        if len(matrix[row]) == 0:
            raise TypeError(message_1)
        for col in range(len(matrix[row])):
            if not isinstance(matrix[row][col], (int, float)):
                raise TypeError(message_1)
    length = []
    for row in range(len(matrix)):
        length.append(len(matrix[row]))
    if not all(elem == length[0] for elem in length):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) == bool:
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            d = matrix[row][col]/div
            d = "{:.2f}".format(d)
            new_matrix[row].append(float(d))
    return new_matrix
