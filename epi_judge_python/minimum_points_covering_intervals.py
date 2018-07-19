import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):
    if not intervals:
        return 0

    min_right = float('inf')
    visits = []

    for inter in intervals:
        if inter.left <= min_right:
            min_right = min(min_right, inter.right)
        else:
            visits.append(min_right)
            min_right = inter.right

    return len(visits)+1


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))
