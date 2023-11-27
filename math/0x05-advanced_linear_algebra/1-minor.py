#!/usr/bin/env python3
"""
Modulus that generates a minors matrix
"""
deter = __import__('0-determinant').determinant


def minor(matrix):
    """Function that calculates miniors matrix

    Args:
        matrix (List of lists): Matrix

    Raises:
        TypeError: matrix must be a list of lists
        ValueError: matrix must be a non-empty square matrix

    Returns:
        list of lists: Matrix of miniors
    """
    if type(matrix) is not list and type(matrix[0]) is not list:
        raise TypeError('matrix must be a list of lists')
    if len(matrix) != len(matrix[0]) or (matrix is None or matrix[0] is None):
        raise ValueError('matrix must be a non-empty square matrix')

    if len(matrix[0]) == 1:
        return [[1]]

    largo = len(matrix)
    retorno = []

    for i in range(largo):
        renglon = []
        for j in range(largo):
            relevante = [[x for a, x in enumerate(row) if a != j] for b,
                         row in enumerate(matrix) if b != i]
            # print(relevante)
            renglon.append(deter(relevante))
        retorno.append(renglon)

    return retorno
