import numpy as np


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
    assert(isinstance(N, int))
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



fib(5)