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
