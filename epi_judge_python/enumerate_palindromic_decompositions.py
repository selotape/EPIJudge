from test_framework import generic_test


def palindrome_decompositions(input):
    results = []

    def decompose(offset, partial_decomposition):
        if offset == len(input):
            results.append(list(partial_decomposition))
            return

        for new_offset in range(offset + 1, len(input) + 1):
            if _is_palindrome(input, offset, new_offset):
                partial_decomposition.append(input[offset:new_offset])
                decompose(new_offset, partial_decomposition)
                partial_decomposition.pop()

    decompose(0, [])
    return results


def _is_palindrome(input, _from, _to):
    while _from < _to:
        if input[_from] != input[_to - 1]:
            return False
        _from, _to = _from + 1, _to - 1
    return True


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
