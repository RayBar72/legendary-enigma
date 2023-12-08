#!/usr/bin/env python3
"""
Modulus that has class Neuron that defines a single
neuron performing binary classification
"""
import numpy as np
import matplotlib.pyplot as plt


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
        Z = np.matmul(self.__W, X) + self.__b
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

    def evaluate(self, X, Y):
        """Function that evaluates neuron

        Args:
            X (ndarray): inputs
            Y (ndarray): correct labels

        Returns:
            ndarray, float: predicted labels, cost
        """
        _ = self.forward_prop(X)
        predict = np.where(self.__A >= 0.5, 1, 0)
        return predict, self.cost(Y, self.__A)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Function that performs gradient descent

        Args:
            X (ndarray): input data
            Y (ndarray): output
            A (ndarray): labels for input data
            alpha (float, optional): learning rate. Defaults to 0.05.
        """
        m = Y.shape[1]
        dzw = - np.matmul((Y - A), X.T) / m
        dzb = - np.sum(Y - A) / (m)
        self.__W = self.__W - alpha * dzw
        self.__b = self.__b - alpha * dzb

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """Function that trains neuron

        Args:
            X (ndarray): input data
            Y (ndarray): labels
            iterations (int, optional): number of iterations. Defaults to 5000.
            alpha (float, optional): learning rate. Defaults to 0.05.

        Raises:
            TypeError: iterations must be an integer
            ValueError: iterations must be a positive integer
            TypeError: alpha must be a float
            ValueError: alpha must be positive

        Returns:
            ndarray, float: predicted labels, cost
        """
        if type(iterations) is not int:
            raise TypeError('iterations must be an integer')
        if iterations < 1:
            raise ValueError('iterations must be a positive integer')
        if type(alpha) is not float:
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')
        if type(step) is not int:
            raise TypeError('step must be an integer')
        if step < 1 or step > iterations:
            raise ValueError('step must be positive and <= iterations')

        costo = []

        for iter in range(iterations + 1):
            predict, C = self.evaluate(X, Y)
            self.__A = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)
            if iter % step == 0:
                print('Cost after {} iterations: {}'.format(iter, C))
            costo.append(C)
        if graph:
            plt.plot(range(0, iterations + 1), costo)
            plt.xlabel('iteratin')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()
        return predict, C
