import unittest

from randm import Randm

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.random = Randm()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.random, Randm)

    def test_decorator_calc(self):
        self.assertIsInstance(self.random, Randm)

    def test_randomrange(self):
        self.assertEqual((Randm.rdmRange(1, 100)), (Randm.rdmRange(1, 100)))

    def test_randomlist(self):
        self.assertTrue(isinstance(Randm.randList(1, 100, 10, 11), list))

    def test_randomselector(self):
        data = Randm.randList(0, 100, 30, 99)
        self.assertTrue(Randm.rdmSelector(data))

    def test_randomNselector(self):
        data = Randm.randList(0, 100, 30, 99)
        self.assertTrue(all(i in data for i in Randm.rdmNselector(data, 3)))

if __name__ == '__main__':
    unittest.main()