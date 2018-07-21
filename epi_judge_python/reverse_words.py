import functools
from itertools import chain

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    s.reverse()

    word_start = 0
    for cur_char, c in enumerate(chain(s, [32])):
        if c == 32:
            reverse_word(s, word_start, cur_char - 1)
            word_start = cur_char + 1


def reverse_word(s, _from, _to):
    for _ in range((_to - _from + 1) // 2):
        s[_from], s[_to] = s[_to], s[_from]
        _from += 1
        _to -= 1


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
