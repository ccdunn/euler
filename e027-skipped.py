"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
import numpy as np
import utils


def solve(N):
    assert(N > 2)
    # at least 2 primes can be generated since a = 0, b = 2 generates 2 primes

    cand_primes = utils.primes_ub(2*(N-1)**2)
    cand_a_primes = utils.primes_ub(2*N)
    cand_bs = cand_a_primes[np.where(cand_a_primes < N)[0]]
    # cand_bs = utils.primes_ub(N)
    cand_a_primes = utils.primes_ub(N + cand_bs[-1] + 1)

    bb = cand_bs[-1]

    cand_as = cand_a_primes[:, np.newaxis] - cand_bs[np.newaxis, :] - 1

    max_n = 1
    for bb in cand_bs:
        for aa in cand_a_primes - bb - 1:
            nn = 1
            while np.in1d(nn**2 + nn*aa + bb, cand_primes)[0]:
                nn += 1
            if nn > max_n:
                max_n = nn
                max_a = aa
                max_b = bb



    mask = np.ones((cand_as.size, cand_bs.size), dtype=bool)

    mask = np.logical_and(mask, )

    nn = 1
    cand_as = cand_as[np.where(cand_as >= (2 - bb - nn**2)//nn)[0]]

    max_n = 1

    mask = np.zeros((cand_as, cand_bs.size))

    2**2 + 2*cand_as + bb


    # b must be prime and positive
    # at most, can generate b primes

    return


def solve_1(N):
    assert(N > 2)
    # at least 2 primes can be generated since a = 0, b = 2 generates 2 primes

    # b must be prime and positive
    # at most, can generate b primes

    cand_primes = utils.primes_ub(2*(N-1)**2)
    cand_a_primes = utils.primes_ub(2*N)
    cand_bs = cand_a_primes[np.where(cand_a_primes < N)[0]]
    # cand_bs = utils.primes_ub(N)
    cand_a_primes = utils.primes_ub(N + cand_bs[-1] + 1)
    # cand_as = (cand_a_primes[:, np.newaxis] - cand_bs[np.newaxis, :] - 1).ravel()
    # cand_bs = (np.repeat(cand_bs[:, np.newaxis], cand_a_primes.size, 1)).ravel()

    cand_as = np.arange(-N, N + 1, dtype=int)
    cand_bs = (np.repeat(cand_bs[:, np.newaxis], cand_a_primes.size, 1))
    cand_as, cand_bs = np.meshgrid(cand_as, cand_bs)
    cand_as = cand_as.ravel()
    cand_bs = cand_bs.ravel()

    nn = 1
    mask = np.in1d(nn**2 + cand_as*nn + cand_bs, cand_primes)

    while np.any(mask):
        cand_as = cand_as[mask]
        cand_bs = cand_bs[mask]

        nn += 1
        mask = np.in1d(nn**2 + cand_as*nn + cand_bs, cand_primes)

    a = cand_as[0]
    b = cand_bs[0]
    print(a)
    print(b)
    print(nn - 1)
    ns = np.arange(nn)
    print(ns**2 + a*ns + b)
    return abs(a*b)


print(solve_1(42))
print(solve_1(1000))

