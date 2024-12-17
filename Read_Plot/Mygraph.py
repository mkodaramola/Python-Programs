import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]  # x-axis values
y = [2, 4, 6, 8, 10]  # y-axis values

# Plot the graph
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph Example')

# Display the graph
plt.show()
