import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data = np.random.normal(loc=50, scale=10, size=1000)

# Create histogram
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

# Add titles and labels
plt.title("Static Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show grid
plt.grid(True)

# Display plot
plt.show()
