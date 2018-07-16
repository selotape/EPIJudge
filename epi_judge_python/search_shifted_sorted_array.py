from test_framework import generic_test


def search_smallest(A):
    return  find_cycle_start(A)
    

def find_cycle_start(A):
    len_A = len(A)
    _from, _to = 0, len_A-1
    while _from < _to:
        mid = (_from + _to)//2
        leftest, rightest, curr = A[_from], A[_to], A[mid]
        if A[(mid-1) % len_A] > A[mid] < A[(mid+1) % len_A]:
            return mid  
        elif curr < rightest:
            _to = mid - 1
        else:
            _from = mid + 1
    return _from

    
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
