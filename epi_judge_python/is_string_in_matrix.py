import functools

from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    n = len(grid)
    m = len(grid[0])

    def adjacencies(i, j):
        for a_i, a_j in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if (a_i, a_j) != (i, j) and 0 <= a_i < n and 0 <= a_j < m:
                yield (a_i, a_j)

    @functools.lru_cache(maxsize=None)
    def can_pattern_start_from(pat, i, j):
        if grid[i][j] != pat[0]:
            return False
        if len(pat) == 1:
            return True

        return any(can_pattern_start_from(pat[1:], a_i, a_j) for a_i, a_j in adjacencies(i, j))

    return any(can_pattern_start_from(tuple(S), i, j) for i in range(n) for j in range(m))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
