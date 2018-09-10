"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""
import numpy as np
import utils


def solve(N):
    ab_nonmult_nums = np.array([], dtype=int)
    ab_nums = np.array([], dtype=int)
    for n in np.arange(1, N + 1, dtype=int):
        if not np.all(np.mod(n, ab_nonmult_nums)):
            ab_nums = np.append(ab_nums, n)
        elif n < np.sum(utils.divisors(n)[:-1]):
            ab_nums = np.append(ab_nums, n)
            ab_nonmult_nums = np.append(ab_nonmult_nums, n)

    K = ab_nums.size
    L = np.where(ab_nums*2 > N)[0][0]
    ab_sums = np.zeros((L**2//2 + L + (K - L)*L, ), dtype=int)
    loc = 0
    for ii in range(L):
        ab_sums[loc:loc + ab_nums.size - ii] = ab_nums[ii] + ab_nums[ii:]
        loc += ab_nums.size - ii

    ab_sums = ab_sums[np.where(ab_sums <= N)[0]]

    return utils.sum_1toN(N) - np.sum(np.unique(ab_sums))


print(solve(28123))

