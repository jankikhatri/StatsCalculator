import random

class Randm:

    def rdmRange(x, y, seed = None):
        if seed is None:
            if (x - y == 1) or (x - y == -1):
                return random.randint(x, y) / 100
            return random.randrange(x, y)
        else:
            random.seed(seed)
            if (x - y == 1) or (x - y == -1):
                return random.randint(x, y) / 100
            return random.randrange(x, y)

    def randList(x, y, N, seed = None):
        if seed is None:
            data = []

            for i in range(N):
                if (x - y == 1) or (x - y == -1):
                    data.append(random.randint(x, y) / 100)
                else:
                    data.append(random.randint(x, y))
            return data
        else:
            data = []

            random.seed(seed)
            for i in range(N):
                if (x - y == 1) or (x - y == -1):
                    data.append(random.randint(x, y) / 100)
                else:
                    data.append(random.randint(x, y))
            return data

    def rdmSelector(data, seed = None):
        if seed is None:
            return data[random.randint(0, len(data) - 1)]
        else:
            return data[random.randint(0, len(data) - 1)]

    def rdmNselector(data, N, seed = None):
        if seed is None:
            return random.sample(data, N)
        else:
            random.seed(seed)
            return random.sample(data, N)