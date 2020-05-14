from randm import Randm

class SystematicSampling:

    @staticmethod
    def sysSampling(x, y, length, frm):
        newdata = []
        data = Randm.randList(x, y, length)
        for i in range(1, y):
            if i*frm < len(data):
                newdata.append(data[i*frm])
        return newdata