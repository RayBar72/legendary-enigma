#!/usr/bin/env python3
"""
Modulas that makes padding convolve for gray scale
"""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """performs a padding convolution on grayscale images

    Args:
        images (np.ndarray): Set of images
        kernel (np.ndarray): Kernel for convolve
        padding (tuple): padding for height and width

    Returns:
        np.ndarray: New convolved array
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    ph, pw = padding
    oh, ow = h - kh + 2 * ph + 1, w - kw + 2 * pw + 1

    out = np.zeros((m, oh, ow))
    print(out.shape)
    paded = np.pad(images, ((0,), (ph,), (pw,)), 'constant')
    print(paded.shape)

    for i in range(oh):
        for j in range(ow):
            out[:, i, j] = np.sum(kernel *
                                  paded[:, i:i + kh, j:j + kw], axis=(1, 2))

    return out
