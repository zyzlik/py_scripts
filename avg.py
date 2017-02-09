"""
Input: sequence of integers, separating by spaces
We should calculate all integers, until we meet 0
Output: average

Example:
Input: 1 2 3 6 0 7 8
We count average only for (1, 2, 3, 6)
Output: 3
"""


import sys

seq = []
line = sys.stdin.readline()


while line.strip() != '0':
    seq.append(int(line.strip()))
    line = sys.stdin.readline()


def avg(iterable):
    return sum(iterable) / float(len(iterable))

sys.stdout.write(str(avg(seq)))
