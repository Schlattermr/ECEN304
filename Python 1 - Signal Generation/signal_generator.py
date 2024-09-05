import matplotlib.pyplot as plt

# Bring in functions from utils file
from utils import generate_sine_wave
from utils import generate_square_wave
from utils import generate_triangle_wave

# Create the values for plots
x_sine, y_sine = generate_sine_wave()
x_square, square_wave = generate_square_wave()
x_triangle, triangle_wave = generate_triangle_wave()

# Create a sine plot
plt.figure(figsize=(20, 5))
plt.subplot(1, 3, 1)
plt.plot(x_sine, y_sine, label='Sine Wave')
plt.title('Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Create a square plot
plt.subplot(1, 3, 2)
plt.plot(x_square, square_wave, label='Square Wave')
plt.title('Square Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Create a square plot
plt.subplot(1, 3, 3)
plt.plot(x_triangle, triangle_wave, label='Triangle Wave')
plt.title('Triangle Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.grid(True)

# Show the plot
plt.show()