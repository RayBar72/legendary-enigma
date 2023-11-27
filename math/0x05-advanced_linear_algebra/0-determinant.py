#!/usr/bin/env python3
"""
Modulus that calculates determinant
"""


def det_rec(matrix):
    """Function that calculates recursibile determinant

    Args:
        matrix (list of lists): Matrix

    Returns:
        int: Determinant
    """
    suma = 0
    if len(matrix) == 2 and len(matrix[0]) == 2:
        suma = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return suma
    else:
        for i in range(len(matrix)):
            aux = [[x for x in row] for row in matrix]
            aux.remove(matrix[0])
            for j in range(len(aux)):
                aux[j] = aux[j][0:i] + aux[j][i + 1:]
            suma += (-1) ** (i % 2) * matrix[0][i] * det_rec(aux)
        return suma


def determinant(matrix):
    """Function that calculates determinant

    Args:
        matrix (list of list): Matrix

    Raises:
        TypeError: matrix must be a list of lists
        ValueError: matrix must be a square matrix

    Returns:
        int: Determinant
    """
    if type(matrix) is not list and type(matrix[0]) is not list:
        raise TypeError('matrix must be a list of lists')

    if matrix == [[]]:
            return 1

    r = len(matrix)
    cols = [len(x) for x in matrix]

    rev = [True if x == r else False for x in cols]

    if not all(rev):
        raise ValueError('matrix must be a square matrix')

    c = len(matrix[0])

    if c == 1:
        return matrix[0][0]

    return det_rec(matrix)
