# -*- encoding: utf8 -*-

# Given a list S, we should check
# if all elements are unique or not


def uniqness_1(seq):
    # 25.3 µs
    s = set(seq)
    return len(s) == len(seq)


def uniqness_2(seq):
    # 18.4 µs
    seq.sort()
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            return False
    return True


def uniqness_3(seq):
    # 2.05 µs
    dct = {}
    for elem in seq:
        if elem in dct:
            return False
        else:
            dct[elem] = True
    return True


def uniqness_4(seq):
    # little bit slower, but still better than others
    dct = {}
    for elem in seq:
        if dct.get(elem):
            return False
        else:
            dct[elem] = True
    return True
