import unittest
import random

from numpy.random import seed
from randm import Randm
from StatisticFunctions.Statistics import Statistics
import pprint
data = Randm.randList(1, 100, 30, 99)

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics()
        self.newdata = data

    def test_instantiate_cal(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        self.assertIsInstance(25.489, Statistics.mean(self, self.newdata))

    def test_mode(self):
        self.assertEqual(120, int(Statistics.mode(self, self.newdata)))

    def test_median(self):
        self.assertEqual(51, Statistics.median(self, self.newdata))

    def test_variance(self):
        self.assertEqual(526, int(Statistics.variance(self, self.newdata)))

    def test_stddev(self):
        self.assertEqual((225, int(Statistics.standardDev(self, self.newdata))))

    def test_zscore(self):
        self.assertTrue(isinstance(Statistics.zscore(self, self.newdata), list))

if __name__ == '__main__':
    unittest.main()