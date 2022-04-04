"""
Given data,
    frequencies = [7, a, 8, 10, 5]
    mid-values  = [5,15,25, 35,45]
The given value of mean is 24.
"""

# Importing the modules
import numpy as np
import math
from sympy import Eq, Symbol, solve

# Making a matrix for frequencies(f) and mid-values(x) WITHOUT the value involving variable 'a'
f_without_a = np.array([7, 8, 10, 5])
x_without_a = np.array([5, 25, 35, 45])

# Making a matrix for frequencies(f) and mid-values(x) WITH the value involving variable 'a'
f_with_a = np.array(["a"])
x_with_a = np.array([15])

# Making 1 vector matrix with required sizes
size_4_1 = np.array([1, 1, 1, 1])
size_1_1 = np.array([1])

# Substituting in the equation, mean = [f.x(without a) + f.x(with a)]/[f.1(without a) + f.1(with a)]
fx_without_a = np.dot(f_without_a, x_without_a)
f1_without_a = np.dot(f_without_a, size_4_1)

# Constructing the equation
a = Symbol('a')
eqn = Eq((fx_without_a + 15*a)/(f1_without_a + a), 24)

# Obtaining and verifying the answer
print("The value of a is",solve(eqn))
