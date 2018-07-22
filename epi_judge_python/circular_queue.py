from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self._data = []
        self._head, self._tail, self._capacity = 0, 0, capacity
        self._resize(capacity)

    def _resize(self, new_capacity):
        items = list(self)
        self._capacity = new_capacity
        self._data = [None] * new_capacity
        self._head, self._tail = 0, 0
        for item in items:
            self._enqueue(item)

    def enqueue(self, x):
        if self.size() == self._capacity:
            self._resize(self._capacity * 2)
        self._enqueue(x)

    def _enqueue(self, x):
        self._data[self._tail % self._capacity] = x
        self._tail += 1

    def dequeue(self):
        if self.size() > 0:
            v, self._data[self._head % self._capacity] = self._data[self._head % self._capacity], None
            self._head += 1
            return v

    def size(self):
        diff = self._tail - self._head
        return diff if diff >= 0 else self._capacity - diff

    def __iter__(self):
        p = self._head
        for _ in range(self.size()):
            v = self._data[p % self._capacity]
            p += 1
            yield v


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
