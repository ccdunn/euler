"""
Project Euler Problem 29
========================

Consider all integer combinations of a^b for 2 a 5 and 2 b 5:

  2^2=4, 2^3=8, 2^4=16, 2^5=32
  3^2=9, 3^3=27, 3^4=81, 3^5=243
  4^2=16, 4^3=64, 4^4=256, 4^5=1024
  5^2=25, 5^3=125, 5^4=625, 5^5=3125

If they are then placed in numerical order, with any repeats removed, we
get the following sequence of 15 distinct terms:

     4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for
2 <= a <= 100 and 2 <= b <= 100?
"""
import utils
import numpy as np


# def solve_0(N):
#     a = np.arange(2, N + 1, dtype=int)
#     b = a[:, np.newaxis]
#     a = a[np.newaxis, :]
#
#     print(np.power(a, b))
#
#     return np.sum(np.logical_not(np.isclose(b - a, loga_b)))


# def solve(N):
#     a = np.arange(2, N + 1, dtype=int)
#     b = a[:, np.newaxis]
#     a = a[np.newaxis, :]
#
#     pow(a, b)
#     logb = np.log(b)
#     loga = np.log(a)
#
#     loga_b = logb/loga
#
#     return np.sum(np.logical_not(np.isclose(b - a, loga_b)))
#
#
# def solve_1(N):
#     factors = [utils.factorize_and_count(n) for n in np.arange(2, N+1, dtype=int)]
#
#     mult = np.math.factorial(int(np.log2(N)))
#
#     maxs = [np.max(fs[1]) for fs in factors]
#     dists = [(fs[1]*mult)//np.max(fs[1]) for fs in factors]
#
#     return (N - 1)**2 - n_dubs


# this is dumb. should be a more elegant way than just always relying on python's amazing int class
# other solution would involve looking at factorization of bases and looking for integer multiples of the counts of the prime factors
def solve_2(N):
    return np.unique([[base**power for base in range(2, N + 1)] for power in range(2, N + 1)]).size


# print(solve_2(5))
# assert(solve_2(5) == 15)
print(solve_2(100))

