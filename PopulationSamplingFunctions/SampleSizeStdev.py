from StatisticFunctions.ZScore import ZScore
from StatisticFunctions.StandardDeviation import StandardDeviation
from PopulationSamplingFunctions.MarginOfError import MarginOfError
from MathOperations.Exponentiation import Exponentiation

class SampleSizestdev:

    @staticmethod
    def samplestdev(data):
        zval = ZScore.zscore(data)
        stdDev = StandardDeviation.stardardDev(data)
        merror = MarginOfError.marginoferror(data)
        num = Exponentiation.power(((zval*stdDev)/(merror/100)),2)
        return round(num, 2)