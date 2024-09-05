import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
# Create an array of 100 evenly spaced values between 0 and 10 (inclusive).
# These values will be used as the x-coordinates for plotting.
x = np.linspace(0, 10, 100)

# Calculate the corresponding y-coordinates using the sine function.
y = np.sin(x)

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)')
plt.title('Simple Plot using numpy and matplotlib')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()