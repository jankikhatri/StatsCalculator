from MathOperations.nthroot import nthroot
from StatisticFunctions.Mean import Mean
from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.ZScore import ZScore
class ConfidenceSample:

    @staticmethod
    def confInterval(data, cval = 0.95):
        mean = Mean.mean(data)
        standardDev = StandardDeviation.stardardDev(data)
        n = len(data)
        zscr = ZScore.zscore(cval)
        num = round(zscr*(standardDev/nthroot.root(2, n)), 2)
        return round((mean - num), 2), round(mean), round((mean + num), 2)