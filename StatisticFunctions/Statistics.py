from Calculator.calculator import Calculator
from StatisticFunctions.Mean import Mean
from StatisticFunctions.Median import Median
from StatisticFunctions.Mode import Mode
from StatisticFunctions.Quartiles import Quartiles
from StatisticFunctions.Skewness import skewness
from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Variance import Variance
from StatisticFunctions.ZScore import ZScore

class Statistics(Calculator):
    result = 0

    def __init__(self):
        pass

    def mean(self, data):
        self.result = Mean.mean(data)
        return self.result

    def median(self, data):
        self.result = Median.med(data)
        return self.result
    
    def mode(self, data):
        self.result = Mode.mode(data)
        return self.result

    def quart(self, data):
        self.result = Quartiles.quartiles(data)
        return self.result

    def skew(self, data):
        self.result = skewness.skewness(data)
        return self.result

    def standardDev(self, data):
        self.result = StandardDeviation.stardardDev(data)
        return self.result

    def variance(self, data):
        self.result = Variance.variance(data)
        return self.result

    def zscore(self, data):
        self.result = ZScore.zscore(data)
        return self.result