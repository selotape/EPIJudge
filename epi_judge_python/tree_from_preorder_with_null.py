import functools

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder):
    if not preorder:
        return None
    return _reconstruct_preorder(preorder, 0)[0]


def _reconstruct_preorder(preorder, _from):
    if preorder[_from] is None:
        return None, 1
    elif preorder[_from + 1] == preorder[_from + 2] == None:
        return BinaryTreeNode(preorder[_from]), 3
    else:
        left, l_size_including_nones = _reconstruct_preorder(preorder, _from + 1)
        right, r_size_including_nones = _reconstruct_preorder(preorder, _from + 1 + l_size_including_nones)
        total_size = 1 + r_size_including_nones + l_size_including_nones
        return BinaryTreeNode(preorder[_from], left, right), total_size


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
