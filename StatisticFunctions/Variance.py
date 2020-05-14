from StatisticFunctions.StandardDeviation import StandardDeviation
from MathOperations.Exponentiation import Exponentiation

class Variance:

    @staticmethod
    def variance(data):
        return Exponentiation.power(StandardDeviation.stardardDev(data), 2)