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
            TypeError: _description_
            ValueError: _description_
        """
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
