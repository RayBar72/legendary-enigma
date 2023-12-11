#!/usr/bin/env python3
"""
Modulus that has class Neural Network for
binary classification
"""
import numpy as np


class NeuralNetwork:
    """
    Class that defines a Neural Network
    """
    def __init__(self, nx, nodes):
        """Function that init class Neural Network

        Args:
            nx (int): number of features
            nodes (int): number of features

        Raises:
            TypeError: nx must be an integer
            ValueError: nx must be a positive number
            TypeError: nodes must be an integer
            ValueError: nodes must be a positive integer
        """
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive number')
        if type(nodes) is not int:
            raise TypeError('nodes must be an integer')
        if nodes < 1:
            raise ValueError('nodes must be a positive integer')

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
        Getter W1
        """
        return self.__W1

    @property
    def b1(self):
        """
        Getter W1
        """
        return self.__b1

    @property
    def A1(self):
        """
        Getter A1
        """
        return self.__A1

    @property
    def W2(self):
        """
        Getter W2
        """
        return self.__W2

    @property
    def b2(self):
        """
        Getter b2
        """
        return self.__b2

    @property
    def A2(self):
        """
        Getter W1
        """
        return self.__A2

    def forward_prop(self, X):
        """Forward propagation function

        Args:
            X (ndarray): Inputs

        Returns:
            ndarray: Outputs
        """
        z1 = self.__W1 @ X + self.__b1
        a1 = 1 / (1 + np.exp(- z1))
        self.__A1 = a1
        z2 = self.__W2 @ self.__A1 + self.__b2
        a2 = 1 / (1 + np.exp(- z2))
        self.__A2 = a2
        return self.__A1, self.__A2

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

    def evaluate(self, X, Y):
        """Function that evaluates neuron

        Args:
            X (ndarray): inputs
            Y (ndarray): correct labels

        Returns:
            ndarray, float: predicted labels, cost
        """
        _ = self.forward_prop(X)
        predict = np.where(self.__A2 >= 0.5, 1, 0)
        return predict, self.cost(Y, self.__A2)
