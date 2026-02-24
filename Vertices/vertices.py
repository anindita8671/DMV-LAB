import matplotlib.pyplot as plt
import numpy as np


n = int(input("Enter the number of vertices: "))


x_coords = np.random.uniform(0, 10, n)
y_coords = np.random.uniform(0, 10, n)


plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, color='green', s=200)  


for i in range(n):
    for j in range(i + 1, n):
        plt.plot([x_coords[i], x_coords[j]], [y_coords[i], y_coords[j]], color='black', linewidth=1)


for i in range(n):
    plt.text(x_coords[i], y_coords[i], str(i+1), color='white',
             fontsize=12, ha='center', va='center', fontweight='bold')


plt.axis('off')

plt.show()
