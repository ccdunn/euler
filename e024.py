"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""
import numpy as np
import utils


def solve(N, K):
    n = N - 1
    bases = np.zeros((K, ), dtype=int)
    nums_left = np.arange(K, dtype=int)
    for k in np.arange(K, dtype=int):
        fac_k = np.math.factorial(K - 1 - k)
        ind = n // fac_k
        n -= ind*fac_k
        bases[k] = nums_left[ind]
        nums_left = np.delete(nums_left, ind)
    # np.array([N//np.math.factorial(k - 1) for k in np.arange(K, 0, -1, dtype=int)])
    return utils.debasify10(bases)


# assert(solve(3, 3) == 102)
print(solve(1000000, 10))

