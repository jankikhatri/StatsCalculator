from Calculator.calculator import Calculator
from PopulationSamplingFunctions.MarginOfError import MarginOfError
from PopulationSamplingFunctions.CochranSampleSize import CochranSampleSize
from PopulationSamplingFunctions.ConfidenceInterval import ConfidenceInterval
from PopulationSamplingFunctions.confidenceSample import ConfidenceSample
from PopulationSamplingFunctions.RandomSampling import randomSample
from PopulationSamplingFunctions.SampleSizeNOstdev import SampleSizeNOstdev
from PopulationSamplingFunctions.SampleSizeStdev import SampleSizestdev
from PopulationSamplingFunctions.SystematicSampling import SystematicSampling

class Sample(Calculator):

    def __init__(self):
        pass

    def randomsmpl(self, x, y, size, osize):
        self.result = randomSample.rsample(x, y, size, oSize)
        return self.result

    def samplesizestd(self, data):
        self.result = SampleSizestdev.samplestdev(data)
        return self.result

    def samplesizenostd(self, data, p = 0.5):
        self.result = SampleSizeNOstdev.samplenostdev(data, p)
        return self.result

    def confInterval(self, data):
        self.result = ConfidenceInterval.confInterval(data)
        return self.result

    def confsample(self, data, cval = 0.95):
        self.result = ConfidenceSample.confInterval(data, cval)
        return self.result

    def marginerror(self, data):
        self.result = MarginOfError.marginoferror(data)
        return self.result

    def cochran(self, data, p = 0.5):
        self.result = CochranSampleSize.cochran(data, p)
        return self.result

    def syssample(self, x, y, size, frm):
        self.result = SystematicSampling.sysSampling(x, y, size, frm)
        return self.result