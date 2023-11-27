#!/usr/bin/env python3
"""
Modulus that generates a adjugate matrix
"""
cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Function that generates a adjugate matrix

    Args:
        matrix (list of lists): Square matrix

    Raises:
        TypeError: matrix must be a list of lists
        ValueError: matrix must be a non-empty square matrix

    Returns:
        list of lists: Adjugate matrix
    """
    if type(matrix) is not list and type(matrix[0]) is not list:
        raise TypeError('matrix must be a list of lists')
    if len(matrix) != len(matrix[0]) or (matrix is None
                                         or matrix[0] is None):
        raise ValueError('matrix must be a non-empty square matrix')

    if len(matrix[0]) == 1:
        return [[1]]

    largo = len(matrix)

    relevante = cofactor(matrix)

    reto = [[relevante[i][j] for i in range(largo)] for j in range(largo)]

    return reto
