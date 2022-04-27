# Importing appropriate libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Constructing a frequency polygon for the data.
Here, we are constructing the histogram for a better visualization before drawing the frequency polygon
Figure_1
"""

# Figure labelling
Fig_1 = plt.figure(1)

# Data given
val = pd.read_excel("values.xlsx","Sheet1",usecols="A",nrows=52)
x1 = np.array(val)

# Advancing the plots
plt.title("Constructing a Histogram of the given data", fontsize=15)
plt.xlim(135, 205)
plt.ylim(0, 21)
plt.grid(alpha=0.45)

#Plotting the histogram values
plt.hist(x1,bins=[140,150,160,170,180,190,200],edgecolor='red',alpha=0.7)
plt.xlabel("Cost of living index", fontsize=15)
plt.ylabel("Number of weeks", fontsize=15)

"""
Constructing a frequency polygon for the data.
Here, we are constructing the required frequency polygon
Figure_2
"""

# Figure labelling
Fig_2 = plt.figure(2)

# The data given
# x-values while plotting the frequency polygon
val = pd.read_excel("values.xlsx","Sheet1",usecols="B",nrows=9)
xe = np.array(val)
x = xe.ravel()

# y-values while plotting the frequency polygon
val = pd.read_excel("values.xlsx","Sheet1",usecols="C",nrows=9)
ye = np.array(val)
y = ye.ravel()

# Limits for the graph parameters
plt.xlim(125, 215)
plt.ylim(0, 21)
plt.grid(alpha=0.45)

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


# Printing the above generated graphs using the python code
plt.show()
