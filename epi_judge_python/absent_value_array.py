from test_framework import generic_test
from test_framework.test_failure import TestFailure
from array import array

def find_missing_element(stream):
    data = list(stream)
    lowerhalf_counts = array('i', (0 for _ in range(2**16)))
    lowerhalf_mask = 2**16-1
    for elem in data:
        lowerhalf = elem & lowerhalf_mask
        lowerhalf_counts[lowerhalf] += 1
    
    jackpot_lowerhalf = next(i for i, count in enumerate(lowerhalf_counts) if count < 2**16)
    
    usedup_upper_halves =  array('b', (0 for _ in range(2**16)))
    for elem in data:
        lowerhalf = elem & lowerhalf_mask
        if lowerhalf == jackpot_lowerhalf:
            print(f'removing {elem}')
            shifted_upperhalf = elem >> 16
            usedup_upper_halves[shifted_upperhalf] = 1
    
    jackpot_upperhalf = next(i for i, flag in enumerate(usedup_upper_halves) if not flag)
    return (jackpot_upperhalf<<16) + jackpot_lowerhalf
    

def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
