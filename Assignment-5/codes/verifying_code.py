# Importing the appropriate library
import random
import numpy as np
import math

# No. of students to be divided
No_of_students = 100

"""
Exercise 16: Question 5: Out of 100 students, two sections of 40 and 60 are formed. If you and your friend are
among the 100 students, what is the probability that
        (i) you both enter the same section?
        (ii) you both enter different sections?
"""

# Defining the combination function
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

# The total cases of me and my friend falling in the A section of 40 members is 40^C_2
# The total cases of me and my friend falling in the B section of 60 members is 60^C_2

# Total number of cases is 100^C_2

# (i) Both of us enter the same section
print("(i) The probablility of me and my friend falling in the same section is ", (nCr(40,2)+nCr(60,2))/nCr(100,2))
print("(ii) The probablility of me and my friend falling in the different section is ", 1-((nCr(40,2)+nCr(60,2))/nCr(100,2)))