from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    candidate, best = None, float('inf')

    while tree:
        data = tree.data
        if data <= k:
            tree = tree.right
        else:
            if data < best:
                candidate, best = tree, data
            tree = tree.left

    return candidate


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
