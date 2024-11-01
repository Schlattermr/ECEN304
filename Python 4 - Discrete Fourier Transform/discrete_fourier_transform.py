# Background

#   A DFT maps discrete time to discrete frequency, gathered
# with N instants seperated by a period of T_s. It does this
# by computing a weighted sum of time instants with complex
# exponentials, and is defined mathematically by this equation: the sum 
# from n=0 to N-1 of x[n] * exp(-jnk(2 * pi / N)). DFTs can be very 
# computationally expensive, since it grows at the inefficient rate of 
# O(N^2). Because of this, faster algorithms, such as the Fast Fourier
# Transform (FFT) have been developed. One way it achieves quicker speeds
# is by utilizing divide and conquer techniques, reducing the size of the 
# input by a factor of 2 each step. This has a rate of O(N * logN) instead.

import matplotlib.pyplot as plt
import numpy as np

from utils import *

f = 5
T = 1

# Two required sampling rates
Fs1 = 5 * f
Fs2 = (3/2) * f

t1 = np.linspace(0, T, int(Fs1 * T), endpoint=False)
t2 = np.linspace(0, T, int(Fs2 * T), endpoint=False)

# Two identical sinusoids with different sampling rates
signal1 = np.sin(2 * np.pi * f * t1)
signal2 = np.sin(2 * np.pi * f * t2)

# Compute the N-point DFT of the first signal, where N here 
# is exactly the number of samples from the sinusoid signal.
N1 = len(signal1)
dft1 = calculate_discrete_fourier_transform(signal1, N1)
dft1_fft = np.fft.fft(signal1, N1)

# Compute the N-point DFT of the first signal, where N is five times 
# (5x) larger than the the number of samples from the sinusoid signal.
N1_padded = 5 * len(signal1)
dft1_padded = calculate_discrete_fourier_transform(signal1, N1_padded)
dft1_padded_fft = np.fft.fft(signal1, N1_padded)

# Compute the N-point DFT of the second signal, 
# where N is exactly the same as the previous item.
dft2 = calculate_discrete_fourier_transform(signal2, N1_padded)
dft2_fft = np.fft.fft(signal2, N1_padded)

# Plot results
