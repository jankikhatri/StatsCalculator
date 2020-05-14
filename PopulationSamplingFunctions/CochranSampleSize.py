from StatisticFunctions.ZScore import ZScore
from PopulationSamplingFunctions.MarginOfError import MarginOfError
from MathOperations.Exponentiation import Exponentiation

class CochranSampleSize:

    @staticmethod
    def cochran(data, p = 0.5):
        mrgnerror = MarginOfError.marginoferror(data)
        q = 1 - mrgnerror
        z = ZScore.zscore(data)

        return (Exponentiation.power(z, 2)*p*q) / Exponentiation.power(mrgnerror, 2)