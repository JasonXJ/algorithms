class PriorityQueue:
    def __init__(self, iterable=None):
        if iterable is None:
            self._data = [None]
        else:
            self._data = [None] + list(iterable)
            self._heapify()


    def max(self):
        return self._data[1]


    def extract_max(self):
        rv = self._data[1]
        self._data[1] = self._data[-1]
        del self._data[-1]
        if len(self._data) > 1:
            self._push_down(1)
        return rv


    def __len__(self):
        return len(self._data) - 1


    def _heapify(self):
        for i in range((len(self._data) + 1) // 2 - 1, 0, -1):
            self._push_down(i)
    

    def _push_down(self, i):
        while True:
            child_index = i * 2
            if child_index >= len(self._data):
                return
            if (child_index + 1 < len(self._data) and
                    self._data[child_index + 1] > self._data[child_index]):
                child_index += 1
            if self._data[child_index] > self._data[i]:
                self._data[child_index], self._data[i] = self._data[i], self._data[child_index]
                i = child_index
            else:
                return


def test():
    import random
    random_state = random.getstate()
    random.seed(0)

    def check(lst):
        sorted_lst = sorted(lst, reverse=True)
        pq = PriorityQueue(lst)
        pq_lst = []
        while len(pq):
            pq_lst.append(pq.extract_max())
        assert sorted_lst == pq_lst


    check(list(range(100)))
    check(list(range(100, -1, -1)))

    # Random test
    sizes = [random.randrange(0, 500) for _ in range(1000)] + list(range(500))
    for size in sizes:
        check([random.random() for _ in range(size)])
        check([random.randrange(0, 500) for _ in range(size)])


    random.setstate(random_state)
