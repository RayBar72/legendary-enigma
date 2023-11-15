#!/usr/bin/env python3
"""
Modulas that makes valid convolve for gray scale
"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """performs a valid convolution on grayscale images

    Args:
        images (np.ndarray): Set of images
        kernel (np.ndarray): Kernel for convolve

    Returns:
        np.ndarray: New convolved array
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    oh, ow = h - kh + 1, w - kw + 1

    out = np.zeros((m, oh, ow))

    for i in range(oh):
        for j in range(ow):
            out[:, i, j] = np.sum(kernel *
                                  images[:, i:i + kh, j:j + kw], axis=(1, 2))

    return out
