"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""
import numpy as np
import utils


def load_data(fn='/Users/cda0201/Documents/euler/data/d022.txt'):
    fid = open(fn, 'r')
    txt = fid.read()
    return txt.strip()[1:-1].split('\",\"')


def solve(fn='/Users/cda0201/Documents/euler/data/d022.txt'):
    names = load_data(fn)
    names.sort()
    sorted_scores = np.array([[np.sum(np.array([ord(letter) for letter in name]) - ord("A") + 1)] for name in names])
    assert(names.index("COLIN") == 938 - 1)
    assert(sorted_scores[names.index("COLIN")] == 53)
    return (np.cumsum(np.ones((1, len(names)), dtype=int))).dot(sorted_scores)[0]



print(solve())
