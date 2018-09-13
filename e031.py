"""
Project Euler Problem 31
========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""
import numpy as np
import utils


british_denoms = np.array([1, 2, 5, 10, 20, 50, 100, 200])


def count_change_rec(N, denoms):
    if N == 0:
        return 1
    if not denoms.size:
        return 0
    return sum([count_change_rec(N - coins, denoms[:-1]) for coins in denoms[-1]*np.arange(0, N//denoms[-1] + 1, dtype=int)])


def solve(N):
    return count_change_rec(N, british_denoms)


# print(solve(5))
# assert(solve(5) == 4)
print(solve(200))

