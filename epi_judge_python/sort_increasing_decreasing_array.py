from sorted_arrays_merge import merge_sorted_arrays
from test_framework import generic_test

_INCREASING = 1
_DECREASING = -1


def sort_k_increasing_decreasing_array(A):
    sorted_arrays, next_sorted_arr = [], []
    direction = _INCREASING
    prev = float('-inf')
    for item in A:
        if continues_direction(item, prev, direction):
            next_sorted_arr.append(item)
        else:
            sorted_arrays.append(next_sorted_arr)
            next_sorted_arr = [item]
            direction *= 1
        prev = item

    sorted_arrays.append(next_sorted_arr)

    return merge_sorted_arrays(sorted_arrays)


def continues_direction(item, prev, direction):
    return item >= prev if direction == _INCREASING else item <= prev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
