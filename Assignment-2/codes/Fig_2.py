# importing the important libraries
import numpy as np
import matplotlib.pyplot as plt

# defining the original function
def f(x):
    return np.sqrt((2*x) - 3)

# defining the inverse function
def f_1(x):
    return (((x**2) + 3)/2)

# defining the mirror axis
def axis(x):
    return x

# forming the plotting axis values
xlist = np.linspace(0, 10, num=1000)

plt.figure(figsize=(5,5),num=0, dpi=120)
# plotting f(x)
y1 = f(xlist)
plt.plot(xlist, y1, label="f(x)")

# plotting inverse of f(x)
y2 = f_1(xlist)
plt.plot(xlist, y2, label="inverse of f(x)")

# plotting the y=x line
plt.plot(xlist, xlist, label="y=x line")

# presenting
plt.title("Plotting all the functions obtained")
plt.xlabel("Values of x")
plt.ylabel("Values of corresponding functions")
plt.xlim(0,10)
plt.ylim(0,10)
plt.grid()
plt.legend()
plt.show()