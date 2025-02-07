#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    new_row = []

    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
    if len(row) != len(matrix[0]):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        for num in row:
            num = num / div
            num = round(num, 2)
            new_row.append(num)
            new_matrix.append(new_row)
    return new_matrix
