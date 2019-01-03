"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""
import numpy as np
import utils


opts = np.arange(1, 10, dtype=int)
opt1 = np.repeat(opts[np.newaxis, :], 9, 0)
opt2 = opt1.T
product_ones = np.mod(opt1 * opt2, 10)
valid_pair_opts = np.logical_and(product_ones != opt1, product_ones != opt2)


def solve(N):

    digits = np.arange(1, N + 1, dtype=int)
    digits1 = digits[np.newaxis, :]
    digits2 = digits[:, np.newaxis]
    digits3 = N - digits1 - digits2

    lb = np.log10(10**(digits1-1 + digits2-1))
    ub = np.log10(10**(digits1 + digits2))
    valid_digits = np.where(np.logical_and(digits3))


    pans = np.array([], dtype=int)
    # neither ones place of multiplicands can be a 1
    # odd times a 5 not allowed, nor is even times a 6
    for ones_1 in np.range(3, 10, dtype=int):
        for ones_2 in np.range(2, ones_1, dtype=int):
            # if (ones_1 == 5 and ones_2 % 2) or (ones_2 == 5 and ones_1 % 2):
            #     continue
            # if ones_1 % 2 and ones_2 % 2:
            #     continue
            ones_prod = (ones_1 * ones_2) % 10
            if ones_prod == ones_1 or ones_prod == ones_2:
                continue
            # six digits left to distribute
            # at most 4 digits per multiplicand
            # must be at least as many digits in product as in largest multiplicand
            # if one multiplicand is one digit, other must be 4 digits
            # A =
            # if one multiplicand is 2 digits, other must 3 digits
            # if one multiplicand is 3 digits, other must be at least 2 digits, at most 3 digits
            # if one multiplicand is 4 digits, other must be 1 digit



    return


def solve_0(N):
    (digits_1, digits_2) = np.meshgrid((np.arange(1, N - 1, dtype=int)))
    digits_2 = np.arange(1, N - 1, dtype=int)[:, np.newaxis]
    digits_3 = N - digits_1 - digits_2

    digits1 = digits[np.newaxis, :]
    digits2 = digits[:, np.newaxis]
    digits3 = N - digits1 - digits2

    

print(solve(9))

