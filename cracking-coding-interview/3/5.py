class StupidQueue:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def push_back(self, data):
        while len(self._stack1):
            self._stack2.append(self._stack1.pop())
        self._stack1.append(data)
        while len(self._stack2):
            self._stack1.append(self._stack2.pop())

    def pop_front(self):
        return self._stack1.pop()

def test_StupidQueue():
    q = StupidQueue()
    values = [1,2,3,4,5]
    for x in values:
        q.push_back(x)
    for x in values:
        assert x == q.pop_front()
