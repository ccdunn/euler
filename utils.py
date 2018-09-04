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

# this is slower than simpler origin version :(
# def primes(N):
#     # output first N primes
#     x = np.zeros((N, ), int)
#     # increment candidate y starting with 2
#     y = 2
#     for n in range(N):
#         # search for next prime
#         while True:
#             flag = False
#             # check if candidate y is divisible by any previous primes
#             for z in x[:n]:
#                 # iterate instead of numpy divide because when N is huge, this early termination could be faster
#                 if y//z == y/z:
#                     flag = True
#                     break
#             # if made it through previous primes without finding a divisor, found a new prime
#             if not flag:
#                 break
#             y += 1
#         x[n] = y
#         y += 1
#
#     return x


# def primes(N):
#     # output first n primes
#     x = -np.ones((N, ), int)
#     # this check means we can go by twos later
#     if N:
#         x[0] = 2
#     y = 3
#     for n in range(1, N):
#         while not np.all(np.mod(y, x[:n])):
#             y += 2
#         x[n] = y
#         y += 2
#
#     return x


def primes(N):
    # output first N primes
    if not N:
        return np.array([], int)
    if N >= 4:
        ub = N*(np.log(N) + np.log(np.log(N))) + 1
    else:
        ub = 6
    x = np.zeros((N, ), int)
    x[0] = 2
    ind = 1
    y = np.arange(3, ub, 2, dtype=int)
    for n in range(y.size):
        if y[n]:
            y[n + y[n]::y[n]] = 0
            x[ind] = y[n]
            ind += 1
            if ind == N:
                break

    return x


# def primes_ub(N):
#     # output primes below N
#     x = np.array([], int)
#     if N > 2:
#         x = np.append(x, 2)
#     y = 3
#     while y < N:
#         while not np.all(np.mod(y, x)):
#             y += 2
#         x = np.append(x, y)
#         y += 2
#     if x[-1] >= N:
#         x = x[:-1]
#
#     return x


def primes_ub(N):
    if N <= 2:
        return np.array([], int)
    y = np.arange(3, N, 2, dtype=int)
    x = np.array([2], int)
    for n in range(y.size):
        if y[n]:
            y[n + y[n]::y[n]] = 0
            x = np.append(x, y[n])

    return x


def basify(x, base=10):
    # convert a number to a list of base powers
    return np.mod(x // (10 ** np.arange(np.floor(np.log(x)/np.log(base)), -1, -1)), base).astype(np.int)


def read_large_int(fn):
    return np.fromfile(fn)