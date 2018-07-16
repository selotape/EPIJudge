from test_framework import generic_test


def search_first_of_k(A, k):
    _from, _to = 0, len(A) - 1
    first = -1
    while _from <= _to:
        middle = (_to + _from) // 2
        val = A[middle]
        if val < k:
            _from = middle + 1
        else:
            if val == k:
                first = middle
            _to = middle - 1
    return first


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
