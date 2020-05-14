from StatisticFunctions.ZScore import ZScore
from PopulationSamplingFunctions.MarginOfError import MarginOfError
from MathOperations.Exponentiation import Exponentiation

class SampleSizeNOstdev:

    @staticmethod
    def samplenostdev(data, p = 0.5):
        zval = ZScore.zscore(data)
        merror = MarginOfError.marginoferror(data)
        q = 1 - p
        pq = p*q
        num = Exponentiation.power((zval/(merror/100)),2)*pq
        return round(num, 2)