import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create a circle
circle = plt.Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

def update(frame):
    circle.center = (frame * 0.1, 5)  # Move circle horizontally
    return circle,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    interval=50,
    blit=True
)

plt.title("Animated Moving Circle")
plt.show()
