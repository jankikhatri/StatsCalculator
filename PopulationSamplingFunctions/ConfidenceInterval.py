from StatisticFunctions.ZScore import ZScore
from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Mean import Mean
from MathOperations.nthroot import nthroot

class ConfidenceInterval:

    @staticmethod
    def confInterval(data):
        zvalue = ZScore.zscore(data)
        stdDev = StandardDeviation.stardardDev(data)
        mean = Mean.mean(data)
        n = len(data)
        num = round(zvalue * (stdDev / nthroot.root(2, n)), 2)
        return round((mean - num), 2), round(mean), round((mean + num), 2)