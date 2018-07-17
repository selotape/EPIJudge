from collections import Counter

from test_framework import generic_test


def can_form_palindrome(s):
    s_counts = Counter(s)
    s_odd_counts = {k: c for k, c in s_counts.items() if c % 2}
    return len(s_odd_counts) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
