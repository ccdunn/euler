import numpy as np
import sys


def sum_1toN(N):
    assert np.mod(N, 1) == 0
    # sum integers from 1 to N
    return int(N*(N+1)/2)


def fib(N):
    # return the nth fibonacci number where fib(1) = 1, fib(2) = 2
    if N <= 2:
        if N == 0:
            return 1
        if N < 0:
            return 0
        return N

    xa = 1
    xb = 2

    for n in np.arange(2, N):
        xb = xa + xb
        xa = xb - xa

    return xb


def fibs(N):
    # return the first n fibonacci numbers where fib(1) = 1, fib(2) = 2
    assert(isinstance(N, (int, np.integer)))
    assert(N>0)
    x = np.zeros((N, ), np.int)
    x[0] = 1
    if N == 1:
        return x
    x[1] = 2

    for n in np.arange(2, N):
        x[n] = x[n - 1] + x[n - 2]

    return x


def fibs_ub(N):
    # upper bounded fib series
    # return the fibonacci numbers below N where fib(1) = 1, fib(2) = 2
    x = np.array([], int)
    if N <= 1:
        return x
    x = np.append(x, 1)
    x = np.append(x, 2)

    while x[-1] < N:
        x = np.append(x, x[-1] + x[-2])

    return x[:-1]


def prime_factors_rec(N, at_least):
    if N == 1:
        return np.array([])
    x = np.array([], int)
    at_most = np.floor(np.sqrt(N))
    for cand in np.arange(at_least, at_most+1, dtype=int):
        if not np.mod(N, cand):
            N_red = N//cand
            while not np.mod(N_red, cand):
                N_red //= cand
            x = np.append(x, cand)
            return np.append(x, prime_factors_rec(N_red, cand + 1))
    return N


def prime_factors(N):
    assert(isinstance(N, (int, np.integer)))
    x = np.array([], int)
    at_least = 2
    at_most = int(np.floor(np.sqrt(N)))
    for cand in np.arange(at_least, at_most+1, dtype=int):
        if not np.mod(N, cand):
            N_red = N//cand
            while not np.mod(N_red, cand):
                N_red //= cand
            x = np.append(x, cand)
            return np.append(x, prime_factors_rec(N_red, cand + 1))
    return N


def primes(N):
    # output first n primes
    x = -np.ones((N, ), int)
    y = 2
    for n in range(N):
        while np.any(np.mod(y, x[:n]) == 0):
            y += 1
        x[n] = y
        y += 1

    return x


def primes_ub(N):
    # output primes below N
    x = np.array([], int)
    y = 2
    while y < N:
        while np.any(np.mod(y, x) == 0):
            y += 1
        x = np.append(x, y)
        y += 1

    return x