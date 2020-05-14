from randm import Randm

class randomSample:

    @staticmethod
    def rsample(x, y, size, outputSize):
        data = Randm.randList(x, y, size)
        return Randm.rdmNselector(data, outputSize)