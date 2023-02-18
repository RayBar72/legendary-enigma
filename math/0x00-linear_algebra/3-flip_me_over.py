#!/usr/bin/env python3


def matrix_transpose(matrix):
    matris = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        matris.append(row)

    return matris
