from collections import defaultdict

from test_framework import generic_test


def find_nearest_repetition(paragraph):
    last_seen = defaultdict(lambda: float('-inf'))
    closest_dist = float('inf')
    for i, word in enumerate(paragraph):
        last_seen_dist = i - last_seen[word]
        if last_seen_dist < closest_dist:
            closest_dist = last_seen_dist
        last_seen[word] = i
    return closest_dist if closest_dist != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
