# -*- coding: utf-8 -*-


def is_even(n):
    """ This function checks if number is even
    without using multiplication, modulo, or division
    operators """

    return bin(n)[-1] == '0'


assert is_even(10) is True
assert is_even(46) is True
assert is_even(800) is True
assert is_even(11) is False
assert is_even(251) is False
assert is_even(913) is False
