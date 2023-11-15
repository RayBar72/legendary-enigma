#!/usr/bin/env python3
"""
Modulas that makes pool
"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """performs a pool

    Args:
        images (np.ndarray): Set of images
        kernel (np.ndarray): Kernel for convolve
        padding (tuple / string): padding for height and width
        stride (tuple): stride used for the sliding

    Returns:
        np.ndarray: New convolved array
    """
    m, h, w, c = images.shape
    kh, kw, = kernel_shape
    sh, sw = stride

    oh = int((h - kh) // sh + 1)
    ow = int((w - kw) // sw + 1)

    out = np.zeros((m, oh, ow, c))
    print(out.shape)

    for i in range(oh):
        for j in range(ow):
            recorte = images[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            if mode == 'avg':
                out[:, i, j] = np.average(recorte, axis=(1, 2), keepdims=False)
            else:
                out[:, i, j] = np.max(recorte, axis=(1, 2), keepdims=False)

    return out
