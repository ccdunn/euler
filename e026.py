"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""
import numpy as np
import utils


def reps(n):
    rems = np.array([10], dtype=int)
    while rems[-1]:
        rems = np.append(rems, (rems[-1] - (rems[-1] // n) * n)*10)
        if np.any(rems[:-1] == rems[-1]):
            return rems.size - np.where(rems == rems[-1])[0][0]

    return 0


def solve(N):
    return np.argmax(np.array([reps(n) for n in np.arange(2, N)])) + 2


# print(solve(11))
# assert(solve(11) == 7)
print(solve(1000))


