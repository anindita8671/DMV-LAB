import matplotlib.pyplot as plt

# Data
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 20, 25]

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Equal aspect ratio ensures circle shape
plt.axis('equal')

plt.title("Fruit Distribution")
plt.show()
