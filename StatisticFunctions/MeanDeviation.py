from StatisticFunctions.Mean import Mean
from MathOperations.Division import Division
from MathOperations.Addition import Addition

class MeanDeviation:

    @staticmethod
    def meanDev(data):

        newlist = []
        meanOfData = Mean.mean(data)

        for i in data:
           newlist.append(abs(i - meanOfData))

        total = Addition.sumList(newlist)
        return Division.divide(total, len(data))