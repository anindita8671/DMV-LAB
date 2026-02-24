import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

categories = []
values = []

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    ax.bar(categories, values)
    ax.set_title("Dynamic Bar Chart using Matplotlib")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")

n = int(input("Enter number of bars: "))

for i in range(n):
    cat = input(f"Enter category {i+1}: ")
    val = int(input(f"Enter value for {cat}: "))

    categories.append(cat)
    values.append(val)

    FuncAnimation(fig, update, frames=1, repeat=False)
    plt.pause(0.5)

plt.show()
