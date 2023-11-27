#!/usr/bin/env python3
"""
Modulus that generates a inverse matrix
"""
deter = __import__('0-determinant').determinant
cofactor = __import__('3-adjugate').adjugate


def inverse(matrix):
    """Function that generates a inverse matrix

    Args:
        matrix (list of lists): Square matrix

    Raises:
        TypeError: matrix must be a list of lists
        ValueError: matrix must be a non-empty square matrix

    Returns:
        List of lists: Inverse matrix if it exists
    """
    if type(matrix) is not list and type(matrix[0]) is not list:
        raise TypeError('matrix must be a list of lists')
    if len(matrix) != len(matrix[0]) or (matrix is None
                                         or matrix[0] is None):
        raise ValueError('matrix must be a non-empty square matrix')

    determinant = deter(matrix)

    if determinant == 0:
        return None

    relevante = cofactor(matrix)

    return [[x / determinant for x in row] for row in relevante]
