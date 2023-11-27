#!/usr/bin/env python3
"""
Modulus that generates a cofactor matrix
"""
mini = __import__('1-minor').minor


def cofactor(matrix):
    """Function that generates a cofactor matrix

    Args:
        matrix (list of lists): Matrix

    Raises:
        TypeError: matrix must be a list of lists
        ValueError: matrix must be a non-empty square matrix

    Returns:
        List of lists: Cofactor matrix
    """
    if type(matrix) is not list and type(matrix[0]) is not list:
        raise TypeError('matrix must be a list of lists')
    if len(matrix) != len(matrix[0]) or (matrix is None or matrix[0] is None):
        raise ValueError('matrix must be a non-empty square matrix')

    if len(matrix[0]) == 1:
        return [[1]]

    m_rel = mini(matrix)
    retorno = []

    for i, x in enumerate(m_rel):
        renglon = []
        for j, y in enumerate(x):
            if i % 2 == 0:
                a = 1
            else:
                a = -1
            if j % 2 == 0:
                b = 1
            else:
                b = -1
            renglon.append(y * a * b)
        retorno.append(renglon)

    return retorno
