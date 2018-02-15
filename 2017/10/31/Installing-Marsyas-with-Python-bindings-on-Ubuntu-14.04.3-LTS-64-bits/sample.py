from pylab import *
import sys
from matplotlib import pyplot
from marsyas import *
from marsyas_util import *
y_data = []
system = marsyas.system_from_script_file("sample.mrs")
while (system.getControl("SoundFileSource/input/mrs_bool/hasData").to_bool()):
    system.tick()
    y_data.extend(system.getControl("Selector/selection/mrs_realvec/processedData").to_realvec())
    y_data[-1] *=  44100 / 1025 # Sampling Rate / FFT Size
plot(range(0, len(y_data)), y_data)
savefig('sample.png')