"""
Construct a frequency polygon for the data.
Here, we are constructing the histogram for a better visualization before drawing the frequency polygon
"""

import matplotlib.pyplot as plt
import numpy as np

# Data given
x = [145,145,145,145,145
    ,155,155,155,155,155,155,155,155,155,155
    ,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165
    ,175,175,175,175,175,175,175,175,175
    ,185,185,185,185,185,185
    ,195,195]
bins=[140,150,160,170,180,190,200]

# Advancing the plots
plt.title("Constructing a Histogram of the given data", fontsize=15)
plt.xlim(135,205)
plt.ylim(0,21)
plt.grid(alpha = 0.45)
plt.xlabel("Cost of living index", fontsize=15)
plt.ylabel("Number of weeks", fontsize=15)

# Plotting the histogram
plt.hist(x,bins,edgecolor ='red')

# Printing it using the above code
plt.show()
