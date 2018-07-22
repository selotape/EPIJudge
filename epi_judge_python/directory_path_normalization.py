from collections import deque

from test_framework import generic_test

_ROOT = ''
_SEP = '/'


def shortest_equivalent_path(path):
    parts = path.split(_SEP)
    res = deque()
    for i, part in enumerate(parts):
        if part == '' and i == 0:
            res.append(_ROOT)
        elif part == '.' or part == '':
            continue
        elif part == '..':
            path_len = len(res)
            if path_len == 0 or res[-1] == '..':
                res.append('..')
            elif path_len > 1:
                res.pop()
            else:
                if res[0] == _ROOT:
                    return []
                else:
                    res.pop()
        elif part.isalnum():
            res.append(part)
        else:
            print('Illegal path part %r' % part)
            return []

    joined_short_path = _SEP.join(res)
    return joined_short_path if joined_short_path else '/'


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
