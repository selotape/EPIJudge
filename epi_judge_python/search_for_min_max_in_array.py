import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    if not A:
        return MinMax(None, None)
    elif len(A) == 1:
        return MinMax(A[0], A[0])
    else:
        return MinMax(*_find_min_max(A))


def _find_min_max(A):
    min_c, max_c = float('inf'), float('-inf')

    for i in range(len(A)//2):
        min_c, max_c = _update_min_max(min_c, max_c, A[i*2], A[i*2+1])

    if len(A) % 2:
        min_c, max_c = _consider_last(min_c, max_c, A[-1])
    return min_c, max_c


def _update_min_max(min_c, max_c, l, r):
    smaller, larger = (l, r) if l < r else (r, l)
    return min(min_c, smaller), max(max_c, larger)


def _consider_last(min_c, max_c, last):
    if last is not None:
        if last < min_c:
            min_c = last
        elif last > max_c:
            max_c = last
    return min_c, max_c


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
