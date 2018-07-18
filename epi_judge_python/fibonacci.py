from functools import lru_cache

from test_framework import generic_test


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
