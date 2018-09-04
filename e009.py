"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import numpy as np
import utils


def solve(N):
    b = np.arange(2, (N - 1)/3, dtype=int)
    a = N*(N/2 - b)/(N - b)
    ind = np.where(np.mod(a, 1) == 0)[0][0]
    b = b[ind]
    a = a[ind]
    return int(a*b*np.sqrt(a**2 + b**2))


# print(solve(12))
assert(solve(12) == 3*4*5)
print(solve(1000))

