import collections
from functools import reduce
from operator import xor

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A):
    n, actual_sum, actual_xor = len(A), 0, 0
    expected_sum = int(n / 2 * (n - 1))
    expected_xor = reduce(xor, range(n))
    for i in A:
        actual_sum += i
        actual_xor ^= i

    duplicate_minus_missing = actual_sum - expected_sum
    for i in A:
        res = consider_duplicate(i, expected_xor, actual_xor, duplicate_minus_missing)
        if res:
            return DuplicateAndMissing(*res)


def consider_duplicate(duplicate, expected_xor, actual_xor, duplicate_minus_missing):
    missing = -1 * (duplicate_minus_missing - duplicate)
    if actual_xor ^ missing ^ duplicate == expected_xor:
        return duplicate, missing


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
