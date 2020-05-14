from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Multiplication import Multiplication
from MathOperations.Division import Division
from MathOperations.Exponentiation import Exponentiation
from MathOperations.nthroot import nthroot
from MathOperations.Logarithm import Logarithm

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Addition.sum(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction.subtract(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication.multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Division.divide(a, b)
        return self.result

    def exponent(self, a, b):
        self.result = Exponentiation.power(a, b)
        return self.result

    def nroot(self, a, b):
        self.result = nthroot.root(a, b)
        return self.result

    def log(self, a, b):
        self.result = Logarithm.log(a, b)
        return self.result

