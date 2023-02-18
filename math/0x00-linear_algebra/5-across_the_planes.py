#!/usr/bin/env python3
largo = __import__('2-size_me_please').matrix_shape


def add_matrices2D(mat1, mat2):
    lmat1 = largo(mat1)
    lmat2 = largo(mat2)

    if lmat1 != lmat2:
        return None

    res = [[i + j for i, j in zip(x, y)] for x, y in zip (mat1, mat2)]

    return res
