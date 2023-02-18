#!/usr/bin/env python3


def mat_mul(mat1, mat2):
    m1r = len(mat1)
    m2r = len(mat2)
    m1c = [len(x) for x in mat1]
    m2c = [len(x) for x in mat2]
    matrix = []

    if len(set(m1c)) != 1:
        return None
    if len(set(m2c)) != 1:
        return None

    if m1c[0] != m2r:
        return None

    for i in range(m1r):
        row = []
        for j in range(m2c[0]):
            x = 0
            for k in range(m2r):
                x += mat1[i][k] * mat2[k][j]
            row.append(x)
        matrix.append(row)

    return matrix
