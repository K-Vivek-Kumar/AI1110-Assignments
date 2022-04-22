import matplotlib.pyplot as plt
import numpy as np

x = [135,145,155,165,175,185,195,205,135]
y = [0,5,10,20,9,6,2,0,0]

plt.xlim(125,215)
plt.ylim(0,21)
plt.grid(alpha = 0.45)

n = ["A", "B", "C", "D", "E", "F", "G", "H"]

plt.scatter(x, y, c="blue")

plt.plot(x,y)

plt.title('Frequency polygon of the data', fontsize=15)
plt.xlabel('Cost of living index', fontsize=15)
plt.ylabel('Number of weeks', fontsize=15)

plt.xticks(x, fontsize=12)

for i, label in enumerate(n):
    plt.annotate(label, (x[i], y[i]), fontsize=15)

plt.fill_between(x, y, 0,color='blue',alpha=0.2)


plt.show()
