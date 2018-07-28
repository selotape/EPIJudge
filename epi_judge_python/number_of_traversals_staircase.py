import functools

from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    return _number_of_ways_to_top(top, maximum_step)


@functools.lru_cache(maxsize=None)
def _number_of_ways_to_top(remaining, k):
    if remaining < 0:
        return 0
    if remaining == 0:
        return 1

    return sum(_number_of_ways_to_top(remaining - step, k)
               for step in range(1, k + 1))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
