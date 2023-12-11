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

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """Function that performs backpropagation

        Args:
            X (ndarray): Input
            Y (ndarray): Labels
            A1 (ndarray): Output first layer
            A2 (ndarray): Output last layer
            alpha (float, optional): Learning rate. Defaults to 0.05.
        """
        m = - 1 / Y.shape[1]
        dZ2 = m * (Y - A2)
        dW2 = np.matmul(dZ2, A1.T)
        db2 = np.sum(dZ2, keepdims=True)
        dZ1 = self.__W2.T @ dZ2 * (A1 * (1 - A1))
        dW1 = dZ1 @ X.T
        db1 = np.sum(dZ1, axis=1, keepdims=True)
        self.__W2 = self.__W2 - alpha * dW2
        self.__b2 = self.__b2 - alpha * db2
        self.__W1 = self.__W1 - alpha * dW1
        self.__b1 = self.__b1 - alpha * db1

    def train(self, X, Y, iterations=5000, alpha=0.05):
        if type(iterations) is not int:
            raise TypeError('iterations must be a positive integer')
        if iterations < 1:
            raise ValueError('iterations must be a positive integer')
        if type(alpha) is not float:
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')
        for iteration in range(iterations):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)
        return self.evaluate(X, Y)
