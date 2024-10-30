import numpy as np
import matplotlib.pyplot as plt

from utils import generate_sine_wave
from utils import generate_square_wave
from utils import generate_triangle_wave
from utils import convolve_1d

# Get signals
x_sine, sine_wave_3Hz = generate_sine_wave(3, 5)
x_square, square_wave_3Hz = generate_square_wave(3, 5)
x_square2, square_wave_1Hz = generate_square_wave(1, 5)
x_triangle, triangle_wave_3Hz = generate_triangle_wave(3, 5)
x_square2_5s = np.linspace(0, 5, len(square_wave_1Hz))

# Get convolutions and linspaces
convolution1 = convolve_1d(square_wave_3Hz, square_wave_1Hz)
convolution2 = convolve_1d(triangle_wave_3Hz, square_wave_1Hz)
convolution3 = convolve_1d(sine_wave_3Hz, square_wave_1Hz)
x_conv1 = np.linspace(0, 5, len(convolution1))
x_conv2 = np.linspace(0, 5, len(convolution2))
x_conv3 = np.linspace(0, 5, len(convolution3))

# Create a sine plot
plt.figure(figsize=(25, 15))
plt.subplot(3, 3, 1)
plt.plot(x_sine, sine_wave_3Hz, label='Sine Wave')
plt.title('3Hz Sine Wave (5s Duration)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Create a square plot
plt.subplot(3, 3, 2)
plt.plot(x_square, square_wave_3Hz, label='Square Wave')
plt.title('3Hz Square Wave (5s Duration)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Create a triangle plot
plt.subplot(3, 3, 3)
plt.plot(x_triangle, triangle_wave_3Hz, label='Triangle Wave')
plt.title('3Hz Triangle Wave (5s Duration)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Create three square plots
plt.subplot(3, 3, 4)
plt.plot(x_square2_5s, square_wave_1Hz, label='Square Wave')
plt.title('1Hz Square Wave (1s Duration)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

plt.subplot(3, 3, 5)
plt.plot(x_square2_5s, square_wave_1Hz, label='Square Wave')
plt.title('1Hz Square Wave (1s Duration)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

plt.subplot(3, 3, 6)
plt.plot(x_square2_5s, square_wave_1Hz, label='Square Wave')
plt.title('1Hz Square Wave (1s Duration)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Create convolution 1 subplot
plt.subplot(3, 3, 7)
plt.plot(x_conv1, convolution1, label='Convolution1')
plt.title('Convolution')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Create convolution 2 subplot
plt.subplot(3, 3, 8)
plt.plot(x_conv2, convolution2, label='Convolution2')
plt.title('Convolution')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Create convolution 3 subplot
plt.subplot(3, 3, 9)
plt.plot(x_conv3, convolution3, label='Convolution3')
plt.title('Convolution')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Show the plot
plt.show()