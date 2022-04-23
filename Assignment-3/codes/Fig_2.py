"""
Construct a frequency polygon for the data.
Here, we are constructing the required frequency polygon
"""

import matplotlib.pyplot as plt
import numpy as np

# The data given
x = [135,145,155,165,175,185,195,205,135]
y = [0,5,10,20,9,6,2,0,0]

# Limits for the graph parameters
plt.xlim(125,215)
plt.ylim(0,21)
plt.grid(alpha = 0.45)

# Defining the vertices of the polygon
n = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Plotting the vertices
plt.scatter(x, y, c="blue")

# Plotting the edges of the polygon
plt.plot(x,y)

# Labelling the axis and the graph
plt.title('Frequency polygon of the data', fontsize=15)
plt.xlabel('Cost of living index', fontsize=15)
plt.ylabel('Number of weeks', fontsize=15)

plt.xticks(x, fontsize=12)

# Labelling the vertices
for i, label in enumerate(n):
    plt.annotate(label, (x[i], y[i]), fontsize=15)

# Shading the area of the polygon
plt.fill_between(x, y, 0,color='blue',alpha=0.2)


# Printing the polygon using the above code
plt.show()
