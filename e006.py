"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
import numpy as np
import utils

def solve_0(N):
    N_2 = N**2
    N_3 = N_2*N
    N_4 = N_2**2
    sq_of_sum = (N_4/2 + N_3 + N_2/2)/2
    sum_of_sq = N_3/3 + N/6 + N_2/2
    return int(sq_of_sum - sum_of_sq)


def solve(N):
    return solve_0(N)


def scratch():
    N = 10
    print(N*(N+1)*(N+2)/3)
    return


# scratch()


# print(solve(10))
assert(solve(10) == 2640)
print(solve(100))
