import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Labels
labels = ['A', 'B', 'C', 'D']

# Initial data
sizes = [25, 25, 25, 25]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    
    # Generate new random values
    new_sizes = np.random.randint(1, 100, len(labels))
    
    ax.pie(new_sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title("Dynamic Pie Chart")

ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()
