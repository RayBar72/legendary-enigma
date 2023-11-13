#!/usr/bin/env python3
"""
Modulus that models a normal distribution
"""


class Normal:
    """
    Class that models an normal distribution
    """
    global pi, e
    pi = 3.1415926536
    e = 2.7182818285

    def __init__(self, data=None, mean=0., stddev=1.) -> None:
        """Init function of class Normal

        Args:
            data (list, optional): List of observations. Defaults to None.
            mean (float, optional): Mean of distribution. Defaults to 0..
            stddev (float, optional): Standar deviation of observation.
                Defaults to 1..

        Raises:
            ValueError: stdde must be a positive
            TypeError: data must be a list
            ValueError: data must contain multiple values
        """
        if data is None:
            if stddev < 0:
                raise ValueError('stdde must be a positive')
            mean = float(mean)
            stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            n = len(data)
            mean = sum(data) / n
            cuad = sum([(x - mean) ** 2 for x in data]) / n
            stddev = cuad ** (1 / 2)
        self.mean = mean
        self.stddev = stddev

    def z_score(self, x):
        """Generates z score

        Args:
            x (float): observation

        Returns:
            float: z score
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Converts from z score to x

        Args:
            z (float): Z score

        Returns:
            float: observation
        """
        return self.stddev * z + self.mean

    def pdf(self, x):
        """Probability density function

        Args:
            x (float): observation

        Returns:
            float: pdf
        """
        exponent = - (1 / 2) * (self.z_score(x) ** 2)
        mult = 1 / (self.stddev * ((2 * pi) ** (1 / 2)))
        return mult * (e ** exponent)

    @staticmethod
    def erf(x):
        """Computes an error function for the cumulative dist

        Args:
            x (float): observation with z score

        Returns:
            float: error function
        """
        exponentes = [1, 3, 5, 7, 9]
        divisores = [1, -3, 10, -42, 216]
        serie = [(x ** i) / j for i, j
                 in zip(exponentes, divisores)]
        sumatoria = sum(serie)
        # print(serie)
        # print(sumatoria)
        return (2 / ((pi) ** (1 / 2))) * sumatoria

    def cdf(self, x):
        """Calculate cumulative distribution function

        Args:
            x (float): observation

        Returns:
            float: cdf
        """
        y = self.z_score(x)
        return (1 / 2) * (1 + Normal.erf(y / (2 ** (1 / 2))))
