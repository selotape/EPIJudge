import operator
from collections import deque
from typing import Sequence

from test_framework import generic_test


def evaluate(expression):
    segments = expression.split(',')
    return _evaluate(segments)


_ops = {
    '*': operator.mul,
    '/': operator.floordiv,
    '+': operator.add,
    '-': operator.sub,
}

def _evaluate(segments: Sequence[str]):
    q = deque()
    for w in segments:
        if w in _ops:
            r = q.pop()
            l = q.pop()
            q.append(_ops[w](l, r))
        else:
            q.append(int(w))
    return q.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
