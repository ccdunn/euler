"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

import utils
import numpy as np


def solve_0(N):
    factors = np.array([], int)
    pfactors = np.arange(0, N+1)
    for n in np.arange(2, N):
        factors = np.append(factors, pfactors[n])
        pfactors[n::n] = pfactors[n::n] // pfactors[n]
    return np.prod(factors)


def solve(N):
    return solve_0(N)


# print(solve(10))
assert(solve(10) == 2520)
print(solve(20))
