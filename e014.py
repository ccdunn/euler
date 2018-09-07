"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import numpy as np
import utils


def collatz_count_dyn(x, bank):
    if x >= bank.size:
        bank = np.append(bank, -np.ones((x - bank.size + 1, ), dtype=int))
    if bank[x] < 0:
        if x % 2:
            y = (3*x + 1)//2
            steps = 2
        else:
            y = x//2
            steps = 1
        while not y % 2:
            y //= 2
            steps += 1
        if y == 1:
            bank[x] += steps
            return bank
        y = (3*y + 1)//2
        bank = collatz_count_dyn(y, bank)
        bank[x] += bank[y] + 3 + steps
    return bank


def collatz_count_loop(x, bank):
    N = bank.size
    if x >= bank.size:
        bank = np.append(bank, -np.ones((x - bank.size + 1, ), dtype=int))
    steps = np.array([x], int)
    y = x
    while y >= N or bank[y] < 0:
        if y % 2:
            y = (3*y + 1)
            steps = np.append(steps, np.array([y]))
        if y < N and bank[y] >= 0:
            break
        y = y//2
        steps = np.append(steps, np.array([y]))
        if y < N and bank[y] >= 0:
            break
        while not y % 2:
            y //= 2
            steps = np.append(steps, np.array([y]))
            if y < N and bank[y] >= 0:
                break
    steps[np.where(steps >= N)[0]] = 0
    bank[np.flip(steps, 0)] = bank[y] + np.arange(0, steps.size)
    return bank


def solve(N):
    bank = -np.ones((N, ), int)
    bank[0:2] = 0
    # if it's less than half of N, may as well have been twice the starting number
    start_0 = N//2
    # if it's one less than a multiple of three, may as well have been a smaller number
    start = int(start_0/3)*3
    for ii in np.arange(start, N, 2):
        bank = collatz_count_loop(ii, bank)
    start = int(start_0/3)*3 + 1
    for ii in np.arange(start, N, 2):
        bank = collatz_count_loop(ii, bank)

    return np.argmax(bank)


# print(collatz_count_dyn(13, np.array([-1, 0]))[13])
# print(solve(100))
# print(solve(1000))
# print(solve(10000))
# print(solve(100000))
print(solve(1000000))
