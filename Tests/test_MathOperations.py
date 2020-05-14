import unittest
from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Multiplication import Multiplication
from MathOperations.Division import Division
from MathOperations.Exponentiation import Exponentiation
from MathOperations.nthroot import nthroot
from MathOperations.Logarithm import Logarithm

class MyTestCase(unittest.TestCase):

    def test_MO_add(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MO_sub(self):
        self.assertEqual(-1, Subtraction.subtract(1, 2))

    def test_MO_mul(self):
        self.assertEqual(2, Multiplication.multiply(1, 2))

    def test_MO_div(self):
        self.assertEqual(2, Division.divide(2, 1))

    def test_MO_exp(self):
        self.assertEqual(8, Exponentiation.power(2, 3))

    def test_MO_nroot(self):
        self.assertEqual(3, nthroot.root(3, 27))

    def test_MO_log(self):
        self.assertEqual(1, Logarithm.log(10, 10))

    def test_MO_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

if __name__ == '__main__':
    unittest.main()