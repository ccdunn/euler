"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""
import numpy as np
import utils

# monday
JAN1_1900_DOW = 1
JAN1_1901_DOW = (1 + 365)% 7

YEAR_DAYS = np.cumsum(np.array([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], dtype=int))
LEAP_YEAR_DAYS = np.cumsum(np.array([0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], dtype=int))


def solve(N):
    count = 0
    rel_jan1_dow = np.mod(JAN1_1901_DOW - N, 7)
    for year in range(1901, 2000+1):
        if (year % 4) and (not (year % 100) or not (year % 400)):
            m1_dow = np.mod(rel_jan1_dow + LEAP_YEAR_DAYS, 7)
        else:
            m1_dow = np.mod(rel_jan1_dow + YEAR_DAYS, 7)

        rel_jan1_dow = m1_dow[-1]
        count += np.sum(m1_dow[:-1] == 0)
    return count

assert(sum([solve(dow) for dow in range(7)]) == 100*12)
print(solve(0))
# print(solve(1))
# print(solve(2))
# print(solve(3))
# print(solve(4))
# print(solve(5))
# print(solve(6))
# print(solve(7))

