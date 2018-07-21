from test_framework import generic_test


def longest_contained_range(A):
    unhandled = set(A)
    best = 0
    while len(unhandled) > 0:
        item = unhandled.pop()
        item_interval_len = _consume_neighbors(item, unhandled)
        best = max(best, item_interval_len)
    return best


def _consume_neighbors(item, unhandled):
    bigger, smaller = item + 1, item - 1
    interval_len = 1
    while bigger in unhandled:
        unhandled.remove(bigger)
        bigger += 1
        interval_len += 1
    while smaller in unhandled:
        unhandled.remove(smaller)
        smaller -= 1
        interval_len += 1

    return interval_len


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
