from MathOperations.Addition import Addition
from MathOperations.Division import Division

class Mean:

    @staticmethod
    def mean(data):
        num = len(data)
        total = Addition.sumList(data)
        return Division.divide(total, num)