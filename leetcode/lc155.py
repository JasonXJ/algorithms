class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        current_min = self.getMin()
        if x < current_min:
            current_min = x
        self.stack.append((x, current_min))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return float('+inf')
        return self.stack[-1][1]


def test():
    x = MinStack()
    x.push(1)
    assert x.top() == 1 and x.getMin() == 1
    x.push(2)
    assert x.top() == 2 and x.getMin() == 1
    x.push(-3)
    assert x.top() == -3 and x.getMin() == -3
    x.pop()
    assert x.top() == 2 and x.getMin() == 1
    x.pop()
    assert x.top() == 1 and x.getMin() == 1
    x.pop()
