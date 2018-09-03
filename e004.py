"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import utils
import numpy as np


def is_pal(x):
    dec = utils.basify(x, 10)
    return np.array_equal(dec, np.flip(dec, 0))


def solve_0(N):
    x = 0
    for a in np.arange(10**N - 1, 10**(N - 1) - 1, -1, int):
        if a*(10**N - 1) < x:
            return x
        for b in np.arange(10**N - 1, a - 1, -1, int):
            if is_pal(a*b):
                x = a*b
                break

    return


def solve(N):
    return solve_0(N)


def scratch():
    print(solve(2))
    return


# scratch()
assert(solve(2) == 9009)
print(solve(3))