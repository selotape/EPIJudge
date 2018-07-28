from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    maxes = [1] * len(A)
    for i in range(len(maxes)):
        candidates = (1 + maxes[j] for j in range(i) if A[j] <= A[i])
        for cand in candidates:
            maxes[i] = max(maxes[i], cand)
    return max(maxes)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
