from test_framework import generic_test
from heapq import *


def online_median(sequence):
    lower_nums, higher_nums = MaxHeap(), MinHeap()
    medians = []
    item = next(sequence, None)
    while item:
        higher_nums.push(item)
        if higher_nums.peek() < lower_nums.peek():
            lower_nums.push(higher_nums.pop())
        
        median = calc_median(higher_nums, lower_nums)
        
        medians.append(median)
        item = next(sequence, None)
    
    return medians

def calc_median(higher_nums, lower_nums):
    if len(higher_nums) > len(lower_nums):
        return higher_nums.peek()
    elif len(higher_nums) < len(lower_nums):
        return lower_nums.peek()
    else:
        return (higher_nums.peek() + lower_nums.peek())/2
class MinHeap:
    def __init__(s, items=None):
        h = []
        if items:
            for item in items:
                s.push(item)
        s._h = h
    def __len__(s):
        return len(s._h)
    def push(s, x):
        heappush(s._h, x)
        print(s._h)
    def pop(s):
        return heappop(s._h)
    def peek(s):
        return s._h[0]

class MaxHeap:
    def __init__(s, items=None):
        s._min_heap = MinHeap(items) if items else MinHeap()

    def __len__(s):
        return len(s._min_heap)
    def push(s, x):
        s._min_heap.push(-x)
    def pop(s):
        return -s._min_heap.pop()
    def peek(s):
        return -s._min_heap.peek()

def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
