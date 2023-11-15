#!/usr/bin/env python3
"""
Modulas that makes same convolve for gray scale
"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """performs a same convolution on grayscale images

    Args:
        images (np.ndarray): Set of images
        kernel (np.ndarray): Kernel for convolve

    Returns:
        np.ndarray: New convolved array
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    oh, ow = h, w
    ph, pw = kh - 1, kw - 1
    ph, pw = int(ph), int(pw)

    out = np.zeros((m, oh, ow))
    print(out.shape)
    paded = np.pad(images, ((0,), (ph,), (pw,)), 'constant')
    print(paded.shape)

    for i in range(oh):
        for j in range(ow):
            out[:, i, j] = np.sum(kernel *
                                  paded[:, i:i + kh, j:j + kw], axis=(1, 2))

    return out
