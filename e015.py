"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""
import utils
import numpy as np


def solve(N):
    return int(np.math.factorial(2*N)/(np.math.factorial(N)**2))


# print(solve(2))
assert(solve(2) == 6)
print(solve(20))