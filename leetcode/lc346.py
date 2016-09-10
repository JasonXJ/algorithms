from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        assert size > 0
        self.size = size
        self.deque = deque()
        self.deque_sum = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.deque) == self.size:
            self.deque_sum -= self.deque.popleft()
        self.deque.append(val)
        self.deque_sum += val
        return float(self.deque_sum) / len(self.deque)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
