#!/usr/bin/env python3
"""
Module that models a exponential distribution
"""

class Exponential:
    """
    Class that models an exponential distribution
    """
    global pi, e
    pi = 3.1415926536
    e = 2.7182818285
    def __init__(self, data=None, lambtha=1) -> None:
        """Function that init a Exponential class

        Args:
            data (list, optional): Distribution data.
            lambtha (int, optional): Mean of distribution.

        Raises:
            ValueError: lambtha must be a positive value
            TypeError: data must be a list
            ValueError: data must contain multiple values
        """
        if data is None:
            if lambtha < 0:
                raise ValueError('lambtha must be a positive value')
            lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            lambtha = 1 / (sum(data) / len(data))
        self.lambtha = lambtha

    def pdf(self, x):
        """Function that calculates the probability density funct

        Args:
            x (int): random var

        Returns:
            float: pdf
        """
        if x <= 0:
            return 0
        return self.lambtha * ((e) ** (- self.lambtha * x))


    def cdf(self, x):
        """Function that calculates the cumulative density funct

        Args:
            x (int): random var

        Returns:
            float: cdf
        """
        if x <= 0:
            return 0
        return 1 - ((e) ** (- self.lambtha * x))
