import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

# Create line plot
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add titles and labels
plt.title("Simple Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show grid
plt.grid(True)

# Display the chart
plt.show()
