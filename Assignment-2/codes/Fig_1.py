"""
Finding the inverse of the function, f(x) = sqrt(2x-3)
"""

# importing the important libraries
import numpy as np
import matplotlib.pyplot as plt

# defining the function
def f(x):
    return np.sqrt((2*x) - 3)

# forming the plotting axis values
xlist = np.linspace(1.5, 100, num=1000)
ylist = f(xlist)

# plotting f(x)
plt.figure(num=0, dpi=120)
plt.plot(xlist,ylist,label="f(x)")
plt.title("Plotting the function")
plt.xlabel("Values of x")
plt.ylabel("Values of f(x)")
plt.grid()
plt.legend()
plt.show()
