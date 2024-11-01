import numpy as np

# Generates a sine wave
def generate_sine_wave(f, duration, amplitude):
    x = np.linspace(0, duration, 1000)
    sine_wave = (np.sin(2 * np.pi * f * x)) * amplitude
    return x, sine_wave

# Generates a square wave
def generate_square_wave(f, duration, amplitude):
    x = np.linspace(0, duration, 1000)
    square_wave = (np.sign(np.sin(2 * np.pi * f * x))) * amplitude
    return x, square_wave

# Generates a triangle wave
def generate_triangle_wave(f, duration, amplitude):
    x = np.linspace(0, duration, 1000)
    shift = 1 / (4 * f) # Shift to center wave on y-axis correctly
    triangle_wave = (2 * np.abs(2 * ((x + shift) * f - np.floor((x + shift) * f + 0.5))) - 1) * amplitude
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

# Calculates Fourier coefficients for Fourier transform
def calculate_fourier_coefficients(signal, t, T, N):
    a_n = []
    b_n = []
    dt = t[1] - t[0]

    # DC offset
    a_0 = (1 / T) * np.sum(signal) * dt

    for n in range(1, N + 1):
        # a_n for cosine terms
        a_n_val = (2 / T) * np.sum(signal * np.cos(2 * np.pi * n * t / T)) * dt
        a_n.append(a_n_val)

        # b_n for sine terms
        b_n_val = (2 / T) * np.sum(signal * np.sin(2 * np.pi * n * t / T)) * dt
        b_n.append(b_n_val)

    return [(a_0, 0)] + list(zip(a_n, b_n))

# Approximates Fourier transform
def approximate_fourier_series(coefficients, N, t, T):
    # Separate a_n and b_n
    a_n, b_n = zip(*coefficients)

    # Start with the a_0 (DC component)
    approx = np.full_like(t, a_n[0])

    # Add harmonic contributions
    for n in range(1, N + 1):
        approx += a_n[n] * np.cos(2 * np.pi * n * t / T) * T
        approx += b_n[n] * np.sin(2 * np.pi * n * t / T) * T

    return approx

def calculate_discrete_fourier_transform(signal, N):
    if N > len(signal):
        signal = np.pad(signal, (0, N - len(signal)), 'constant')
    elif N < len(signal):
        raise ValueError("N must be at least as long as the length of the input signal")

    # Compute the DFT using the DFT formula
    dftCoefficients = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            dftCoefficients[k] += signal[n] * np.exp(-1j * n * k * 2 * np.pi / N)

    return dftCoefficients