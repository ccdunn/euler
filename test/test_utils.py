import numpy as np
from utils import *


def test_utils():
    assert(fib(10) == 89)

    assert(sum_1toN(100) == np.sum(np.arange(1, 100 + 1)))

    assert(np.array_equal(prime_factors(169), np.array([13])))

    assert(np.array_equal(prime_factors(16), np.array([2])))

    assert(np.array_equal(prime_factors(13195), np.array([5, 7, 13, 29])))

    assert(np.array_equal(primes(5), np.array([2, 3, 5, 7, 11])))

    assert(np.array_equal(primes_ub(12), np.array([2, 3, 5, 7, 11])))

test_utils()