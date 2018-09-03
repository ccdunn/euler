"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from utils import *


def solve_0(N):

    return np.sum(np.concatenate((np.arange(3, N, 15),
    np.arange(5, N, 15),
    np.arange(6, N, 15),
    np.arange(9, N, 15),
    np.arange(10, N, 15),
    np.arange(12, N, 15),
    np.arange(15, N, 15)), 0))


def solve_1(N):

    return 3*sum_1toN(np.floor((N - 1)/3)) + 5*sum_1toN(np.floor((N - 1)/5)) - 15*sum_1toN(np.floor((N - 1)/15))


def solve(N):
    return solve_1(N)

assert(solve(10) == 23)
print(solve(1000))
