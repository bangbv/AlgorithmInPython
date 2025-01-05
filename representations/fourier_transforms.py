# import scipy and numpy
from scipy.fftpack import fft, ifft
import numpy as np

x = np.array(np.arange(10))
gfg_transformed = fft(x)
# Using scipy.ifft() method
gfg_inversed = ifft(gfg_transformed)

print(gfg_inversed)
