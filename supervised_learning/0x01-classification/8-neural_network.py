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

        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((1, nodes))
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0
