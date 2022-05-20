# Importing the appropriate library
import numpy as np
from matplotlib import pyplot as plt

"""
Exercise 13.4 Question 1
State which of the following are not
the probability distributions of a random variable.
Give reasons for your answer,
We can plot the PMF and CDF for the following values.
"""

plt.rcParams["figure.figsize"] = [9, 4]
plt.rcParams["figure.autolayout"] = True


# Problem no. (i)
Prob_1 = plt.figure(1)

plt.subplot(1, 2, 1)
X = [0,1,2]
Y = [0.4,0,-0.2]
Z = np.cumsum(Y)
plt.xticks(X)
plt.stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.title('PMF for the problem')
plt.grid()
plt.tight_layout()

plt.subplot(1, 2, 2)
data = np.array([0,0,1,1,2])
count, bins_count = np.histogram(data, bins=10)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.title('CDF for the problem')
plt.plot(bins_count[1:], cdf, label="CDF")
plt.grid()
plt.legend()

# Problem no. 2
Prob_2 = plt.figure(2)

plt.subplot(1, 2, 1)
X = [0,1,2,3,4]
Y = [0.1,0.4,-0.3,-0.3,0.4]
Z = np.cumsum(Y)
plt.xticks(X)
plt.stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.title('PMF for the problem')
plt.grid()
plt.tight_layout()

plt.subplot(1, 2, 2)
data = np.array([0,1,1,1,1,1,2,2,4,4,4])
count, bins_count = np.histogram(data, bins=10)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.title('CDF for the problem')
plt.plot(bins_count[1:], cdf, label="CDF")
plt.grid()
plt.legend()

# Problem no. (iii)
Prob_3 = plt.figure(3)

plt.subplot(1, 2, 1)
X = [-1,0,1]
Y = [0.6,-0.5,0.1]
Z = np.cumsum(Y)
plt.xticks(X)
plt.stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.title('PMF for the problem')
plt.grid()
plt.tight_layout()

plt.subplot(1, 2, 2)
data = np.array([-1,-1,-1,-1,-1,-1,0,1,1])
count, bins_count = np.histogram(data, bins=10)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.title('CDF for the problem')
plt.plot(bins_count[1:], cdf, label="CDF")
plt.grid()
plt.legend()

# Problem no. (iv)
Prob_4 = plt.figure(4)

plt.subplot(1, 2, 1)
X = [-1,0,1,2,3]
Y = [0.3,-0.1,0.2,-0.3,-0.05]
Z = np.cumsum(Y)
plt.xticks(X)
plt.stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.title('PMF for the problem')
plt.grid()
plt.tight_layout()


plt.subplot(1, 2, 2)
data = np.array([0,1,1,1,1,2,2,3,3,3])
count, bins_count = np.histogram(data, bins=10)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.title('CDF for the problem')
plt.plot(bins_count[1:], cdf, label="CDF")
plt.grid()

plt.legend()
plt.show()