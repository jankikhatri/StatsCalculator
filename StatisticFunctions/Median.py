class Median:

    @staticmethod
    def med(data):
        n = len(data)
        data.sort()

        if n % 2 == 0:
            median1 = data[n // 2]
            median2 = data[n // 2 - 1]
            return (median1 + median2)/2

        else:
            return data[n // 2]