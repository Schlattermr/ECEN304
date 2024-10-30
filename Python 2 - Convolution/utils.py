import numpy as np

# Generates a sine wave
def generate_sine_wave(f, duration):
    x = np.linspace(0, duration, 1000)
    y = np.sin(2 * np.pi * f * x)
    return x, y

# Generates a square wave
def generate_square_wave(f, duration):
    x = np.linspace(0, duration, 1000)
    square_wave = np.sign(np.sin(2 * np.pi * f * x))
    return x, square_wave

# Generates a triangle wave
def generate_triangle_wave(f, duration):
    x = np.linspace(0, duration, 1000)
    shift = 1 / (4 * f) # Shift to center wave on y-axis correctly
    triangle_wave = 2 * np.abs(2 * ((x + shift) * f - np.floor((x + shift) * f + 0.5))) - 1
    return x, triangle_wave

# Convolves waves 
def convolve_1d(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    # Max possible length for a convolution with these sizes
    max = n + m - 1

    # Initialize resulting array to zeros
    result = np.zeros(max)

    # Convolution operation
    for i in range(max):
        for j in range(m):
            if i - j >= 0 and i - j < n:
                result[i] += arr1[i - j] * arr2[j]

    return result