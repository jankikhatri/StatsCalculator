from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.ZScore import ZScore
from MathOperations.nthroot import nthroot

class MarginOfError:

    @staticmethod
    def marginoferror(data):

        standardDev = StandardDeviation.stardardDev(data)
        zscr = abs(ZScore.zscore(data))
        n = len(data)

        return zscr*(standardDev/(nthroot.root(2, n)))