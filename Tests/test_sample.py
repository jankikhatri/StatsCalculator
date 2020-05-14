import unittest
from PopulationSamplingFunctions.Sample import Sample
from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Mean import Mean
from randm import Randm

class MyTestCase(unittest.TestCase):

    list1 = [10, 20, 30, 40, 50, 60, 70, 80]

    def setUp(self):
        self.sample = Sample()
        self.list1 = Randm.randList(1, 100, 30, 99)
        self.size = len(self.list1)
        self.standarddev = StandardDeviation.stardardDev(self.list1)
        self.merror = 3
        self.mean = Mean.mean(self.list1)

    def test_instantiate_sample(self):
        self.assertIsInstance(self.sample, Sample)

    def test_random(self):
        self.assertEqual(len(Sample.randomsmpl(1, 100, 25, 7)), 7)

    def test_samplesizestd(self):
        self.assertEqual(268530.49, Sample.samplesizestd(0.9, self.standarddev, 3))

    def test_samplesizenostd(self):
        self.assertEqual(1506.72, Sample.samplesizenostd(self, 0.95, self.merror, 0.5))

    def test_confinterval(self):
        self.assertEqual((24.6, 30, 44), Sample.confInterval(self, self.list1))

    def test_confsample(self):
        self.assertEqual((24.6, 30, 44), Sample.confsample(self, self.list1, 0.95))

    def test_marginerror(self):
        self.assertEqual(5.617, Sample.marginerror(self, self.list1))

    def test_cochran(self):
        self.assertEqual(70.85, Sample.cochran(self, self.list1, 0.5))

    def test_syssample(self):
        self.assertTrue(isinstance(Sample.syssample(self, 1, 100, 100, 30), list))

if __name__ == '__main__':
    unittest.main()
