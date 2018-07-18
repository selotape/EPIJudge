from test_framework import generic_test


def number_of_ways(n, m):
    cells = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        cells[n-1][i] = 1
    for i in range(n):
        cells[i][m-1] = 1

    for i in reversed(range(0, n - 1)):
        for j in reversed(range(0, m - 1)):
            cells[i][j] = cells[i + 1][j] + cells[i][j + 1]

    return cells[0][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
