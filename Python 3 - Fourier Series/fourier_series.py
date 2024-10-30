import numpy as np
import matplotlib.pyplot as plt

from utils import *

f = 5
T = 1 / f
harmonics = [1, 3, 5, 7]
t, square_wave = generate_square_wave(f, 1, 2)

# Plot the original square wave
plt.plot(t, square_wave, label="Original Square Wave", color='black', linewidth=2)

# Plot Fourier approximations for each value of L in harmonics
for L in harmonics:
    coefficients = calculate_fourier_coefficients(square_wave, t, T, L)
    approx = approximate_fourier_series(coefficients, L, t, T)
    plt.plot(t, approx, label=f"{L} Harmonics")

plt.title("Fourier Series Approximation of a Square Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend(loc="upper right")
plt.grid(True)
plt.show()