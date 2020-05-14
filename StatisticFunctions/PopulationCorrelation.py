from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Mean import Mean

class popcorrelation:
    
    @staticmethod
    def popcorrelation(data1, data2):
        covxy = 0
        n = 0
        xmean = Mean.mean(data1)
        ymean = Mean.mean(data2)
        xstd = StandardDeviation.stardardDev(data1)
        ystd = StandardDeviation.stardardDev(data2)
        if(len(data1) == len(data2)):
            for x, y in zip(data1, data2):
                n += 1
                covxy += abs((int(x-xmean)*int(y-ymean))/n)

        return covxy/(xstd*ystd)