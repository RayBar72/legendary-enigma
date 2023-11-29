#!/usr/bin/env python3
"""
Modulus that has class Neuron that defines a single
neuron performing binary classification
"""
import numpy as np


class Neuron:
    """
    Class Neuron that defines a single neuron performing binary
    classification
    """
    def __init__(self, nx):
        """Function that init class neuron

        Args:
            nx (int): number of

        Raises:
            TypeError: nx must be an integer
            ValueError: nx must be a positive integer
        """
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        Getter of W
        """
        return self.__W

    @property
    def b(self):
        """
        Getter of b
        """
        return self.__b

    @property
    def A(self):
        """
        Getter of A
        """
        return self.__A

    def forward_prop(self, X):
        """Function that executesw forward propagation

        Args:
            X (ndarray): shape (nx, m) containing input data

        Returns:
            ndarray: output of neuron
        """
        Z = np.matmul(self.W, X) + self.b
        A = 1 / (1 + np.exp(-Z))
        self.__A = A
        return self.__A

    def cost(self, Y, A):
        """Function that calculates cost

        Args:
            Y (ndarray): Real data
            A (ndarray): Forcated data

        Returns:
            float: cost
        """
        m = Y.shape[1]
        C = np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        C = - (1 / m) * C
        return C
