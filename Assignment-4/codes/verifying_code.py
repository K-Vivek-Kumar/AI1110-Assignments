# Importing the appropriate library
import random
import numpy as np

# Defining the no, of times we would be doing the experiment in the part i and ii.
No_of_times = 10000

"""
Question 25(i)
Here, in this code, we are verifying the practical value of the probability of
obtaining both heads, both tails or either of them on flipping two coins at a time.
Coin has two sides, head and tail, which are both equally probable.
During this experiment, head corresponds to one and tail corresponds to zero.
"""

# Flipping on each coin correspondingly
Coin1 = np.random.choice([0, 1], size=(No_of_times))
Coin2 = np.random.choice([0, 1], size=(No_of_times))


# Counting the number of times we obtained both heads
"""
If both are heads and each head = 1, then when we obtain both heads
The sum from both coins must be equal to 2.
"""
only_heads = np.count_nonzero((Coin1 + Coin2) == 2)
prob_of_both_heads = only_heads/No_of_times


# Counting the number of times we obtained both tails
"""
If both are tails and each tail = 0, then when we obtain both tails
The sum from both coins must be equal to 0.
"""
only_tails = np.count_nonzero((Coin1 + Coin2) == 0)
prob_of_both_tails = only_tails/No_of_times

# Counting the number of times we obtained one head and one tail
"""
If we get a head and a tail where head = 1 and tail = 0, then their sum will be 1.
"""
one_head_one_tail = np.count_nonzero((Coin1 + Coin2) == 1)
prob_of_each_one = one_head_one_tail/No_of_times


# Printing the practical results
print("Exercise 15.1 Question 25(i) : Two coins problem")
print("   The probability of obtaining both heads in the practical experiment is ",prob_of_both_heads)
print("   The probability of obtaining both tails in the practical experiment is ",prob_of_both_tails)
print("   The probability of obtaining one head and one tail in the practical experiment is ",prob_of_each_one)

"""
Question 25(ii)
Here, in this code, we are verifying the practical value of the probability of
obtaining an odd number or an even number on throwing a die.
Die has six faces, each numbered from 1 to 6 and when rolled, the face on the top is taken into consideration.
The die isn't biased and have equal dimensions from all faces.
"""

# Defining the no, of times we would be doing the experiment
No_of_times = 10000

# Functioning for counting the obtained random number on the top of the die using the function 'random'
T = np.random.choice([1, 2, 3, 4, 5, 6], size=(No_of_times))

# Counting the number of odd numbers
Odd_obtained = np.count_nonzero(T == 1) + np.count_nonzero(T == 3) + np.count_nonzero(T == 5)
prob_of_odd = Odd_obtained/No_of_times

# Counting the number of even numbers
Even_obtained = np.count_nonzero(T == 2) + np.count_nonzero(T == 4) + np.count_nonzero(T == 6)
prob_of_even = Even_obtained/No_of_times

# Printing the practical results
print("Exercise 15.1 Question 25(ii) : One die problem")
print("   The probability of obtaining an odd number in the practical experiment is ",prob_of_odd)
print("   The probability of obtaining an even number in the practical experiment is ",prob_of_even)

# Conclusion
print("We can check that the values we obtained are quite close to the theoretical values.")