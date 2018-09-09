"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""
import numpy as np
import utils


def solve(N):
    return np.sum(utils.basify10(np.math.factorial(N)))


print(solve(100))

