"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
from math import sqrt
from os import killpg

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    #length of the list
    N = 0
    for i in x:
      N += 1
  
    #sum of all elements (x) in the list
    sum_x = 0
    for j in range(N):
      sum_x += x[j]

    #calculate mean
    mean = sum_x / N

    #squared deviations and variance
    squared_dev = 0
    for k in range(N):
      squared_dev += ((x[k] - mean) ** 2)

    variance = squared_dev / N

    return sqrt(variance)


def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    N = len(x)
    # mean
    mean = sum(x) / N
    
    # squared deviations and variance
    squared_dev = sum(xi ** 2 for xi in x) / N
    
    variance = squared_dev - mean ** 2
    return sqrt(variance)


# Approach 3: Using NumPy's std()
import numpy as np

def std_numpy(x):
    return np.std(x)

# Test with a given list of numbers
num_lst = [1, 2, 3, 4, 5]

# Calculate standard deviation using all approaches
std_loop = std_loops(num_lst)
std_builtin = std_builtin(num_lst)
std_np = std_numpy(num_lst)

print(f"Standard Deviation (loops): {std_loop}")
print(f"Standard Deviation (built-in): {std_builtin}")
print(f"Standard Deviation (NumPy): {std_np}")
    