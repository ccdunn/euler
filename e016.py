"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import numpy as np
import utils


def solve(N):
    return np.sum(utils.basify10(2**N))


# print(solve(15))
# assert(solve(15) == 26)
print(solve(1000))
