from test_framework import generic_test, test_utils


def combinations(n, k):
    if n == 0 or k == 0:
        return [[]]

    results = []

    def future_combinations(offset, partial_comb):
        if len(partial_comb) == k:
            results.append(list(partial_comb))
            return

        if offset > n:
            return

        future_combinations(offset + 1, partial_comb)

        partial_comb.append(offset)
        future_combinations(offset + 1, partial_comb)
        partial_comb.pop()

    future_combinations(1, [])
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
