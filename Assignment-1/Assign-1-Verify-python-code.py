"""
Given data,
    frequencies = [7, a, 8, 10, 5]
    mid-values  = [5,15,25, 35,45]
Therefore the value of fi*xi is [35, 15a, 200, 350, 225]
        and the sum of all fi*xi is 810 + 15a.
And the sum of all frequencies are 30 + a.
The given value of mean is 24.
Therefore, the required equation is 24 = (810 + 15a)/(30 + a)
"""

from sympy import Eq, Symbol, solve

a = Symbol('a')
eqn = Eq(24, (810 + 15*a)/(30 + a))

# prints the required value of a.
print(solve(eqn))
