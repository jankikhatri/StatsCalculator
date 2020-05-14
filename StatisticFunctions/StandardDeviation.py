from StatisticFunctions.Mean import Mean
from MathOperations.Addition import Addition
from MathOperations.Division import Division
from MathOperations.nthroot import nthroot
from MathOperations.Exponentiation import Exponentiation

class StandardDeviation:

    @staticmethod
    def stardardDev(data):
        n = len(data)
        mn = Mean.mean(data)
        newlist = []

        for i in data:
            newlist.append(Exponentiation.power(i - mn, 2))

        total = Addition.sumList(newlist)
        return nthroot.root(2, Division.divide(total, n))