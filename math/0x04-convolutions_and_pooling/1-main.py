#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import tensorflow.keras as K
convolve_grayscale_same = __import__('1-convolve_grayscale_same').convolve_grayscale_same


if __name__ == '__main__':

    (x_train, y_train), (x_test, y_test) = K.datasets.mnist.load_data(path='mnist.npz')
    images = x_train
    print(images.shape)
    kernel = np.array([[1 ,0, -1], [1, 0, -1], [1, 0, -1]])
    images_conv = convolve_grayscale_same(images, kernel)
    print(images_conv.shape)

    plt.imshow(images[0], cmap='gray')
    plt.show()
    plt.imshow(images_conv[0], cmap='gray')
    plt.show()
