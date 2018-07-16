from math import isclose

from test_framework import generic_test


def square_root(x):
    if x in (0.0, 1.0):
        return x
    _from = 0.0
    _to = x if x >= 1.0 else 1.0
    mid = (_from + _to) / 2
    mid_squared = mid ** 2
    while not isclose(mid_squared, x, abs_tol=0.0000000000000000001):
        if mid_squared > x:
            _to = mid
        else:
            _from = mid
        mid = (_from + _to) / 2
        mid_squared = mid ** 2

    return mid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
