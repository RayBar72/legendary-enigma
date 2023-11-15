#!/usr/bin/env python3
"""
Modulas that makes convolve for gray scale
"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """performs a convolution on grayscale images

    Args:
        images (np.ndarray): Set of images
        kernel (np.ndarray): Kernel for convolve
        padding (tuple / string): padding for height and width
        stride (tuple): stride used for the sliding

    Returns:
        np.ndarray: New convolved array
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    if type(padding) is str:
        if padding == 'valid':
            ph, pw = 0, 0
        if padding == 'same':
            ph = int(((h - 1) * sh - h + kh) // 2)
            pw = int(((w - 1) * sw - w + kw) // 2)
    else:
        ph, pw = padding

    oh = int((h - kh + 2 * ph) // sh + 1)
    ow = int((w - kw + 2 * pw) // sw + 1)

    out = np.zeros((m, oh, ow))
    print(out.shape)
    paded = np.pad(images, ((0,), (ph,), (pw,)), 'constant')
    print(paded.shape)

    for i in range(oh):
        for j in range(ow):
            out[:, i, j] = np.sum(kernel *
                                  paded[:, i * sh:i * sh + kh,
                                        j * sw:j * sw + kw], axis=(1, 2))

    return out
