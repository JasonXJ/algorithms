# Range Minimum Query algorithms.

class RMQ:
    """ An implementation of the constant query time and linearithmic space (so
    the building time is also linearithmic) solution. See
    https://en.wikipedia.org/wiki/Range_minimum_query#Solution_using_constant_time_and_linearithmic_space
    . """

    def __init__(self, seq):
        if len(seq) == 0:
            self.table = []
            return

        # self.table[i][j] is the minimum value of seq[i:i+2**j]
        self.table = [
            [seq[i]] for i in range(len(seq))
        ]
        j_global_max_plus_1 = len(seq).bit_length()
        for j in range(1, j_global_max_plus_1):
            half_size = 1 << (j - 1)
            for i in range(len(seq) - (1 << j) + 1):
                self.table[i].append(min(
                    self.table[i][j-1],
                    self.table[i + half_size][j-1]
                ))


    def rangemin(self, start, end=None):
        if end is None:
            end = len(seq)
        if end <= start:
            raise ValueError

        # The two ranges we are considering has a size of
        # ``2**floor(log2(end - start))``, so ``j = floor(log2(end-start))``.
        # Here we use ``bit_length`` method to compute j directly.
        j = (end - start).bit_length() - 1

        return min(self.table[start][j], self.table[end - (1 << j)][j])



def test_RMQ():
    import random
    rstate = random.getstate()
    random.seed(0)


    class NaiveRMQ:
        def __init__(self, seq):
            self.table = {}
            for i in range(len(seq)):
                for j in range(i + 1, len(seq) + 1):
                    self.table[(i, j)] = min(seq[i:j])


        def rangemin(self, start, end):
            return self.table[(start, end)]


    def check(seq):
        rmq = RMQ(seq)
        naive_rmq = NaiveRMQ(seq)
        for start in range(len(seq)):
            for end in range(start + 1, len(seq) + 1):
                assert rmq.rangemin(start, end) == naive_rmq.rangemin(start, end)

    
    TIMES = 5
    SIZE_MAX = 100

    # Test increasing sequences
    for size in range(SIZE_MAX):
        check(list(range(size)))

    # Test decreasing sequences
    for size in range(SIZE_MAX):
        check(list(range(size, 0, -1)))

    # Test sequences with only one value
    for size in range(SIZE_MAX):
        check([random.randrange(SIZE_MAX)] * size)

    # Test random sequences
    for _ in range(TIMES):
        for size in range(SIZE_MAX):
            check([random.randrange(SIZE_MAX) for _ in range(size)])


    random.setstate(rstate)


def test_RMQ_simple():
    rmq4 = RMQ([0,1,2,3])
    assert rmq4.table == [
        [0, 0, 0],
        [1, 1],
        [2, 2],
        [3],
    ]
    assert rmq4.rangemin(0,1) == 0
    assert rmq4.rangemin(0,4) == 0
    assert rmq4.rangemin(2,4) == 2

    rmq5 = RMQ([0,1,2,3,4])
    assert rmq5.table == [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2],
        [3, 3],
        [4],
    ]
    assert rmq5.rangemin(0,1) == 0
    assert rmq5.rangemin(0,4) == 0
    assert rmq5.rangemin(0,5) == 0
    assert rmq5.rangemin(2,4) == 2
    assert rmq5.rangemin(2,5) == 2


    rmq5_2 = RMQ([5,3,7,5,1])
    assert rmq5_2.table == [
        [5, 3, 3],
        [3, 3, 1],
        [7, 5],
        [5, 1],
        [1],
    ]
    assert rmq5_2.rangemin(0,1) == 5
    assert rmq5_2.rangemin(0,4) == 3
    assert rmq5_2.rangemin(0,5) == 1
    assert rmq5_2.rangemin(2,4) == 5
    assert rmq5_2.rangemin(2,5) == 1


    rmq8 = RMQ([4,5,3,8,5,6,9,7])
    assert rmq8.table == [
        [4, 4, 3, 3],
        [5, 3, 3],
        [3, 3, 3],
        [8, 5, 5],
        [5, 5, 5],
        [6, 6],
        [9, 7],
        [7],
    ]
    assert rmq8.rangemin(0,1) == 4
    assert rmq8.rangemin(0,2) == 4
    assert rmq8.rangemin(0,3) == 3
    assert rmq8.rangemin(0,4) == 3
    assert rmq8.rangemin(0,5) == 3
    assert rmq8.rangemin(2,4) == 3
    assert rmq8.rangemin(3,5) == 5
    assert rmq8.rangemin(0,8) == 3


