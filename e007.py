"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
import utils
import numpy as np


def solve_0(N):
    return utils.primes(N)[-1]


def solve(N):
    return solve_0(N)


# print(solve(6))
assert(solve(6) == 13)
print(solve(10001))
