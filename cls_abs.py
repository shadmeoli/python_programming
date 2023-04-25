class Computation:


    def __init__(self):
        self.acc = 0

    def add(self):
        self.acc += 1
        return self.acc

    @staticmethod
    def sub(x, y):
        return x-y


print(Computation.sub(5, 2))
print(Computation().add())