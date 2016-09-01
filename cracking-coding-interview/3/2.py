class MinTrackStack:
    """ A stack which track the current minimum value.
    
    Implementation
    --------------

    Whenever push an item into the stack that smaller than the current minimum,
    we record that item as the new minimum. In addition, an extra object of
    type ``MinTrackStack._MinChanged`` will also be pushed on top of the stack
    to record the old minimum.

    Note that if we use an extra stack to record all historical minimums and
    determine if the minimum is changed at a point by comparing two stacks'
    top, handle the case when a new pushed item *equal* to current minimums
    correctly (For implementation of `MinTrackStack`, we do *not* need to do
    anything in the "equal" case.)

    """
    class _MinChanged:
        def __init__(self, old_min):
            self.old_min = old_min

    def __init__(self):
        self._data = []
        self._current_min = None

    def min(self):
        return self._current_min

    def push(self, value):
        self._data.append(value)
        if self._current_min is None or value < self._current_min:
            self._data.append(self._MinChanged(self._current_min))
            self._current_min = value

    def pop(self):
        to_return = self._data.pop()
        if isinstance(to_return, self._MinChanged):
            self._current_min = to_return.old_min
            return self._data.pop()
        return to_return

if __name__ == '__main__':
    s = MinTrackStack()
    for x in [10, 11, 9, 8, 7, 20]:
        s.push(x)
    assert s.min() == 7 and s.pop() == 20
    assert s.min() == 7 and s.pop() == 7
    assert s.min() == 8 and s.pop() == 8
    assert s.min() == 9 and s.pop() == 9
    assert s.min() == 10 and s.pop() == 11
    assert s.min() == 10 and s.pop() == 10

    print('All test passed')
