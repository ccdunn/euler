"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import utils
import numpy as np

def solve_0(N):
    return utils.prime_factors(N)[-1]


def solve_1(N):
    # garbage. takes forever to find all the primes obviously...
    assert(isinstance(N, (int, np.integer)))
    cands = np.flip(utils.primes_ub(int(np.floor(np.sqrt(N)))), 0)
    for cand in cands:
        if not np.mod(N, cand):
            return cand
    return N


def solve(N):
    return solve_0(N)


def scratch():
    print(solve(13195))
    return


# scratch()
assert(solve(13195) == 29)
print(solve(600851475143))
