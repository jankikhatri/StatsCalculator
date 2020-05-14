from StatisticFunctions.Mean import Mean
from StatisticFunctions.StandardDeviation import StandardDeviation

class ZScore:

    @staticmethod
    def zscore(data):
        newData = []
        mean = Mean.mean(data)
        stdDev = StandardDeviation.stardardDev(data)
        for i in data:
            newData.append((i - mean)/stdDev)

        return newData