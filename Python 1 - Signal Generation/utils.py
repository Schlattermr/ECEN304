import numpy as np

# Values set to control frequency of the waves
f = 2
w = 2 * np.pi * f

# Generates a sine wave using numpy functions
def generate_sine_wave():
    x = np.linspace(0, 5, 1000)
    sine_wave = np.sin(w * x)
    return x, sine_wave

# Generates a square wave using numpy functions
def generate_square_wave():
    x = np.linspace(0, 5, 1000)
    square_wave = np.sign(np.sin(w * x))
    return x, square_wave

# Generates a triangle wave using numpy functions
def generate_triangle_wave():
    x = np.linspace(0, 5, 1000)
    triangle_wave = 2 * np.abs(2 * (x * f - np.floor(x * f + 0.5))) - 1
    return x, triangle_wave
