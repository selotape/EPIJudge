from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    last_seen = {}
    best = 0
    subarray_size = 0

    for i, item in enumerate(A):
        if _item_in_current_subarray(i, subarray_size, last_seen, item):
            subarray_size = i - last_seen[item]
        else:
            subarray_size += 1
        best = max(best, subarray_size)
        last_seen[item] = i

    return best


def _item_in_current_subarray(i, subarray_size, last_seen, item):
    if item not in last_seen:
        return False
    subarray_start = i - subarray_size
    return subarray_start <= last_seen[item]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
