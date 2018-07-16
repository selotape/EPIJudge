from heapq import *

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
    return list(_merge_sorted_arrays(sorted_arrays))


def _merge_sorted_arrays(arrs):
    h = []
    iters = [iter(arr) for arr in arrs]

    for i, _iter in enumerate(iters):
        item = next(_iter, None)
        if item is not None:
            heappush(h, (item, i))

    while h:
        min_item, min_iter_ix = heappop(h)
        yield min_item
        new_item = next(iters[min_iter_ix], None)
        if new_item is not None:
            heappush(h, (new_item, min_iter_ix))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
