from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Mean import Mean

class samplecorrelation:

    @staticmethod
    def samplecorrelation(data1, data2):
        numerator = 0
        n = 0
        meanofx = Mean.mean(data1)
        meanofy = Mean.mean(data2)
        stdevx = StandardDeviation.stardardDev(data1)
        stdevy = StandardDeviation.stardardDev(data2)
        if len(data1) == len(data2):
            for x, y in zip(data1, data2):
                n += 1
                numerator += abs((int(x - meanofx) * int(y - meanofy)) / (n - 1))

        return numerator / (stdevx * stdevy)