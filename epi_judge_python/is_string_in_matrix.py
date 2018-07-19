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
    def can_pattern_start_from(offset, i, j):
        if grid[i][j] != S[offset]:
            return False
        new_offset = offset+1
        if new_offset == len(S):
            return True

        return any(can_pattern_start_from(new_offset, a_i, a_j) for a_i, a_j in adjacencies(i, j))

    return any(can_pattern_start_from(0, i, j) for i in range(n) for j in range(m))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
