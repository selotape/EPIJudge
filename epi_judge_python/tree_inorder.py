from test_framework import generic_test


def inorder_traversal(tree):
    return list(inorder_O1_space(tree))


def inorder_O1_space(t):
    prev = None
    while t:
        if prev is t.parent:
            if t.left:
                _next = t.left
            else:
                yield t.data
                _next = t.right or t.parent
        elif prev is t.left:
            yield t.data
            _next = t.right or t.parent
        else:  # prev is t.right
            _next = t.parent
        prev, t = t, _next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
