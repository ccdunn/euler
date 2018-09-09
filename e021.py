"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import numpy as np
import utils


def d(n):
    return np.sum(utils.divisors(n)[:-1])


assert(d(220) == 284)
assert(d(284) == 220)
assert(d(d(284)) == 284)
assert(d(d(220)) == 220)


def solve(N):
    count = 0
    for n in np.arange(2, N):

        dtmp = d(n)
        if dtmp != n and d(dtmp) == n:
            count += n
    return count


print(solve(10000))

