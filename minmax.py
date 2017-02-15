# -*- coding: utf-8 -*-


def minmax(seq):
    """ This function tuple of integers of min and max
    values of given sequence without using built-in min
    and max functions """

    seq.sort()

    return (seq[0], seq[-1])


assert minmax([1, 2, 3]) == (1, 3)
assert minmax([8, 1, 5]) == (1, 8)
