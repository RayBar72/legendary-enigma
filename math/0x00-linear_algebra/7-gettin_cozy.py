#!/usr/bin/env python3
largo = __import__('2-size_me_please').matrix_shape


def cat_matrices2D(mat1, mat2, axis=0):
    retorno = []


    if axis == 0:
        for x, y in zip(mat1, mat2):
            if len(x) != len(y):
                return None
        retorno = [[x for x in row] for row in mat1]
        for x in mat2:
            retorno.append(x)
        return retorno
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        for x, y in zip(mat1, mat2):
            retorno.append(x + y)
        return retorno
    else:
        return None
