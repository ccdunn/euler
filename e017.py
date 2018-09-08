"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""
import numpy as np
import utils


ones_text = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
teens_text = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
tens_text = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

ones_lens = np.array([len(text) for text in ones_text])
teens_lens = np.array([len(text) for text in teens_text])
tens_lens = np.array([len(text) for text in tens_text])

lets100 = np.concatenate((ones_lens, teens_lens, (tens_lens[2:, np.newaxis] + np.reshape(ones_lens, (1, -1))).ravel()), 0)

ands = len('and')*np.ones((100, ), dtype=int)
ands[0] = 0
lets100to1000 = len('hundred') + (ones_lens[1:, np.newaxis] + np.reshape(lets100 + ands, (1, -1))).ravel()
lets1000 = np.concatenate((lets100, lets100to1000), 0)

assert(lets1000[342] == 23)
assert(lets1000[115] == 20)
assert(lets1000[800] == len('eight hundred'.replace(" ", "")))
assert(lets1000[100] == len('one hundred'.replace(" ", "")))
assert(lets1000[898] == len('eight hundred and ninety eight'.replace(" ", "")))

# def under100count(bases):
#
#     if bases.size < 2:
#         return ones_lens[bases[-1]]
#     and_flag = np.any(bases[:-2])
#     if bases[-2] >= 2:  # x at least twenty, no weirdness
#         return and_flag * len('and') + tens_lens[bases[-2]] + ones_lens[bases[-1]]
#     if bases[-2] >= 1:  # x in teens
#         return and_flag * len('and') + teens_lens[bases[-1]]
#     # x in ones
#     return and_flag * len('and') + ones_lens[bases[-1]]


def under100counts():
    if bases.size < 2:
        return ones_lens[bases[-1]]
    thous_lets = 0 if bases.size <= 3 else ones_lens[bases[-3]] + (np.any(bases[-6:-3])) * len('thousand')
    hunds_lets = 0 if bases.size <= 2 else ones_lens[bases[-2]] + (np.any(bases[-6:-3])) * len('hundred')
    and_flag = np.any(bases[:-2]) and np.any(bases[-2:])
    lets = thous_lets + hunds_lets + and_flag
    if bases[-2] >= 2:  # x at least twenty, no weirdness
        lets += tens_lens[bases[-2]] + ones_lens[bases[-1]]
    elif bases[-2] >= 1:  # x in teens
        lets += teens_lens[bases[-1]]
    else:    # x in ones
        lets += ones_lens[bases[-1]]
    return lets


def under10000count(bases):
    if bases.size < 2:
        return ones_lens[bases[-1]]
    thous_lets = 0 if bases.size <= 3 else ones_lens[bases[-3]] + (np.any(bases[-6:-3])) * len('thousand')
    hunds_lets = 0 if bases.size <= 2 else ones_lens[bases[-2]] + (np.any(bases[-6:-3])) * len('hundred')
    and_flag = np.any(bases[:-2]) and np.any(bases[-2:])
    lets = thous_lets + hunds_lets + and_flag
    if bases[-2] >= 2:  # x at least twenty, no weirdness
        lets += tens_lens[bases[-2]] + ones_lens[bases[-1]]
    elif bases[-2] >= 1:  # x in teens
        lets += teens_lens[bases[-1]]
    else:    # x in ones
        lets += ones_lens[bases[-1]]
    return lets


def solve_0(N):
    assert(N < 1000000)
    lets = 0
    for ii in np.arange(1, N + 1, dtype=int):
        lets += under10000count(utils.basify10(ii))

    return lets


def solve_1(N):
    assert(N < 100000)
    # extras
    lets = np.sum(lets1000[:np.mod(N, 1000) + 1])
    if N >= 1000:
        # extras
        lets += np.sum(lets1000[1:N//1000 + 1] + len('thousand'))

        # all else in full thousands
        lets += np.sum(lets1000) * (np.sum(lets1000[1:N//1000 + 1] + len('thousand')))
    return lets


def solve_2(N):
    if N == 1000:
        return np.sum(lets1000) + len('one thousand'.replace(" ", ""))
    return np.sum(lets1000[:N + 1])


def solve(N):
    return solve_2(N)


# print(solve(5))
assert(solve(5) == 19)
# print(solve(1000) - solve(999))
assert(solve(1000) - solve(999) == len('one thousand'.replace(" ", "")))
print(solve(1000))


