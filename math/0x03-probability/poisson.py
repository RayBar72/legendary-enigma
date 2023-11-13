#!/usr/bin/env python3
"""
Modulos that creates a class for a Poisson distribution
"""


class Poisson:
    global e
    e = 2.7182818285
    def __init__(self, data=None, lambtha=1) -> None:
        """Function that inits Poission class

        Args:
            data (list, optional): Data. Defaults to None.
            lambtha (int, optional): Mean of Poisson distribution. Defaults to 1.

        Raises:
            ValueError: lambtha must be a positive value
            TypeError: data must be a list
            ValueError: data must contain multiple values
        """
        if data is None:
            if not lambtha > 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = sum(data) / len(data)

    @staticmethod
    def facto(k):
        """Function that calculates factorial

        Args:
            k (int): Number for that facotrial has to be calc

        Returns:
            int: Factorial
        """
        if k <= 1:
            return 1
        return k * Poisson.facto(k - 1)

    def pmf(self, k):
        """Function that calculates the probability mass function

        Args:
            k (int): Number of occurrences

        Returns:
            float: pmf
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        mult = (self.lambtha ** k) * (e ** (- self.lambtha))
        div = Poisson.facto(k)
        return mult / div

    def cdf(self, k):
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        reto = 0
        for i in range(k + 1):
            reto += self.pmf(i)
        return reto
