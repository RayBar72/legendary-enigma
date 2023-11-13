#!/usr/bin/env python3
"""
Modulus tha models a binomial distribution
"""


class Binomial:
    """
    Class that models a binomial distribution
    """
    def __init__(self, data=None, n=1, p=0.5) -> None:
        """Init for binomial distribution

        Args:
            data (list, optional): List with data. Defaults to None.
            n (int, optional): Number of trials. Defaults to 1.
            p (float, optional): Probability of successes. Defaults to 0.5.

        Raises:
            ValueError: n must be a positive value
            ValueError: p must be a greater than 0 an less than 1
            TypeError: data must be a list
            ValueError: data must contain multiple values
        """
        if not data:
            if n < 0:
                raise ValueError('n must be a positive value')
            if p > 1 or p < 0:
                raise ValueError('p must be a greater than 0 an less than 1')
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            largo = len(data)
            mu = sum(data) / largo
            sigma_2 = sum([(x - mu) ** 2 for x in data]) / largo
            p = 1 - (sigma_2 / mu)
            n = int(round(mu / p, 0))
            p = mu / n
        self.p = p
        self.n = n

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
        return k * Binomial.facto(k - 1)

    def pmf(self, k):
        """Calculates the probability mass function

        Args:
            k (int): Number of successes

        Returns:
            float: probability
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        f = Binomial.facto
        n_k = f(self.n) / (f(k) * (f(self.n - k)))
        return n_k * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates cumulative distribution function

        Args:
            k (int): Number of successes

        Returns:
            float: probability
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        acum = 0
        for i in range(k + 1):
            acum += self.pmf(i)
        return acum
