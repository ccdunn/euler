"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import utils
import numpy as np


def solve_1(N):
    y = np.arange(0, N, dtype=int)
    y[1] = 0
    sum = 0
    for n in np.arange(2, N, dtype=int):
        if y[n]:
            y[n::n] = 0
            sum += n

    return sum


def solve_0(N):
    return np.sum(utils.primes_ub(N))


def solve(N):
    return solve_1(N)


# print(solve(10))
assert(solve(10) == 17)
# print(solve(1000))
print(solve(2000000))
