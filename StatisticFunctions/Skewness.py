from StatisticFunctions.Mean import Mean
from StatisticFunctions.Median import Median
from StatisticFunctions.StandardDeviation import StandardDeviation

class skewness:

    @staticmethod
    def skewness(data):

        mean = Mean.mean(data)
        median = Median.med(data)
        stdDev = StandardDeviation.stardardDev(data)
        return (3*(mean - median))/stdDev