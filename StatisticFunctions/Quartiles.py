from StatisticFunctions.Median import Median

class Quartiles:

    @staticmethod
    def quartiles(data):
        count = 0
        for i in list:
            count += 1

        median = Median.med(data)

        if (count % 2) == 0:
            q1 = median/2
            q2 = median + q1

        else:
            q1 = median/2
            q2 = median + q1

        return [q1, median, q2]