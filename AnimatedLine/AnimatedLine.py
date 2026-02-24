import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

x = np.linspace(0, 10, 100)
y = np.sin(x)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(x),
    init_func=init,
    interval=50,
    blit=True
)

plt.title("Animated Growing Line")
plt.show()
