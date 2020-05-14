import unittest
from Calculator.calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_cal_return_sum(self):
        result = self.calculator.add(1, 2)
        self.assertEqual(3, result)

    def test_cal_return_diff(self):
        result = self.calculator.subtract(1, 2)
        self.assertEqual(-1, result)

    def test_cal_return_mul(self):
        result = self.calculator.multiply(1, 2)
        self.assertEqual(2, result)

    def test_cal_return_div(self):
        result = self.calculator.divide(2, 1)
        self.assertEqual(2, result)

    def test_cal_return_expo(self):
        result = self.calculator.exponent(2, 3)
        self.assertEqual(8, result)

    def test_cal_return_nroot(self):
        result = self.calculator.nroot(3, 27)
        self.assertEqual(3, result)

    def test_cal_return_log(self):
        result = self.calculator.log(10, 10)
        self.assertEqual(1, result)

    def test_cal_access_sum_result(self):
        self.calculator.add(1, 2)
        self.assertEqual(3, self.calculator.result)

    def test_cal_access_diff_result(self):
        self.calculator.subtract(1, 2)
        self.assertEqual(-1, self.calculator.result)

    def test_cal_access_mul_result(self):
        self.calculator.multiply(1, 2)
        self.assertEqual(2, self.calculator.result)

    def test_cal_access_div_result(self):
        self.calculator.divide(2, 1)
        self.assertEqual(2, self.calculator.result)

    def test_cal_access_exp_result(self):
        self.calculator.exponent(2, 3)
        self.assertEqual(8, self.calculator.result)

    def test_cal_access_nroot_result(self):
        self.calculator.nroot(3, 27)
        self.assertEqual(3, self.calculator.result)

    def test_cal_access_log_result(self):
        self.calculator.log(10, 10)
        self.assertEqual(1, self.calculator.result)

    def test_multiple_cal(self):
        cal1 = Calculator()
        cal2 = Calculator()
        self.calculator.add(cal1.add(1, 2), cal2.subtract(3, 4))
        self.assertEqual(2, self.calculator.result)

if __name__ == '__main__':
    unittest.main()