# -*- coding: utf-8 -*-


def squares(n):
    """ This function returns sum of squares of all positive
    numbers smaller than given positive integer """

    return sum(i**2 for i in range(1, n))


assert squares(4) == 14
