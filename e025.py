"""
Project Euler Problem 25
========================

The Fibonacci sequence is defined by the recurrence relation:

  F[n] = F[n[1]] + F[n[2]], where F[1] = 1 and F[2] = 1.

Hence the first 12 terms will be:

  F[1] = 1
  F[2] = 1
  F[3] = 2
  F[4] = 3
  F[5] = 5
  F[6] = 8
  F[7] = 13
  F[8] = 21
  F[9] = 34
  F[10] = 55
  F[11] = 89
  F[12] = 144

The 12th term, F[12], is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
import numpy as np
import utils

# different def of fib sequence from previous problems which is annoying


def solve(N):
    f1 = 1
    f2 = 1
    t = np.zeros((N, ), dtype=int)
    t[0] = 1
    thresh = utils.debasify10(t)
    count = 2
    while f2 < thresh:
        ftmp = f1
        f1 = f2
        f2 = ftmp + f2
        count += 1

    return count


assert(solve(3) == 12)
print(solve(1000))
