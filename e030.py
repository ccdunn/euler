"""
Project Euler Problem 30
========================

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

  1634 = 1^4 + 6^4 + 3^4 + 4^4
  8208 = 8^4 + 2^4 + 0^4 + 8^4
  9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""
import numpy as np
import utils


def solve(N):
    vmax = 1
    while (10**vmax - 1)/vmax <= 9**N:
        vmax += 1
    nmax = vmax*9**N
    cands = np.arange(2, nmax, dtype=int)
    return sum(cands[[cand == np.sum(utils.basify10(cand) ** N) for cand in cands]])


# print(solve(4))
# assert(solve(4) == 19316)
print(solve(5))

