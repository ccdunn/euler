"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""
import numpy as np
import utils


def solve_0(N):
    assert(N % 2)
    assert(N>0)
    assert(not (N % 1))
    R = N//2
    s = 1 # count 1 once apparently
    # left side of each ring is average of four numbers on diagonal
    for r in np.arange(1, R, dtype=int):
        s += ((2*r + 1)**2)*4
    return


def solve_1(N):
    assert(N % 2)
    assert(N>0)
    assert(not (N % 1))
    # number of rings
    R = N//2
    return int(4*(4*utils.sum_sq_1toN(R) + utils.sum_1toN(R) + R) + 1)


# def sum_1toN(N):
#     assert np.mod(N, 1) == 0
#     # sum integers from 1 to N
#     return int(N*(N+1)/2)
#
#
# def sum_sq_1toN(N):
#     # sum of sq from 1 to N = N*(N+1)*(N-1)/3 + N*(N+1)/2
#     return N**3/3 + N/6 + N**2/2


def solve(N):
    # assert(N % 2)
    # assert(N > 0)
    # assert(not (N % 1))
    # number of rings
    R = N//2
    R_2 = R*R
    return 16*(R_2*R - R)//3 + 10*(R_2+R) + 4*R + 1

# print(solve_1(5))
# assert(solve(5) == 101)
print(solve(1001))

