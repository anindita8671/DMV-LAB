import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure
fig, ax = plt.subplots()

data = []

def update(frame):
    # Simulate new incoming value
    new_value = np.random.normal(50, 10)
    data.append(new_value)

    ax.clear()
    ax.hist(data, bins=20, color='skyblue', edgecolor='black')
    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

ani = animation.FuncAnimation(
    fig,
    update,
    interval=500  # Update every 500ms
)

plt.show()
