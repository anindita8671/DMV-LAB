import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x
y4 = x**2

# Create 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1, 'r')
axs[0, 0].set_title("Sine Wave")

axs[0, 1].plot(x, y2, 'g')
axs[0, 1].set_title("Cosine Wave")

axs[1, 0].plot(x, y3, 'b')
axs[1, 0].set_title("Linear")

axs[1, 1].plot(x, y4, 'm')
axs[1, 1].set_title("Quadratic")

# Adjust spacing
plt.tight_layout()
plt.show()
