import random
from random import randrange

def quicksort(lst):
    def quicksort_(lo, hi):
        if lo >= hi:
            return
        tmp = randrange(lo, hi)
        lst[tmp], lst[hi-1] = lst[hi-1], lst[tmp]
        x = lst[hi-1]
        i = j = lo
        while j < hi - 1:
            if lst[j] < x:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
            j += 1
        lst[i], lst[hi-1] = lst[hi-1], lst[i]
        quicksort_(lo, i)
        quicksort_(i+1, hi)

    quicksort_(0, len(lst))


def quicksort_3ways(lst):
    """ Quicksort with 3-ways partitions, which should perform better when the
    list contain many duplicates. Also note that this is the one-pivot version.
    """
    def partition3(lo, hi):
        if lo >= hi:
            return
        tmp = randrange(lo, hi)
        lst[tmp], lst[hi-1] = lst[hi-1], lst[tmp]
        x = lst[hi-1]
        i = j = k = lo
        while k < hi - 1:
            y = lst[k]
            if y <= x:
                lst[j], lst[k] = lst[k], lst[j]
                j += 1
            if y < x:
                lst[i], lst[j-1] = lst[j-1], lst[i]
                i += 1
            k += 1
        lst[j], lst[hi-1] = lst[hi-1], lst[j]
        partition3(lo, i)
        partition3(j+1, hi)

    partition3(0, len(lst))


def mergesort(lst):
    # NOTE: we can reduce the extra space to ``len(lst) // 2``
    buf = [None] * len(lst)
    def mergesort_(lo, hi):
        if hi - lo <= 1:
            return
        mi = (lo + hi) >> 1
        mergesort_(lo, mi)
        mergesort_(mi, hi)
        buf[lo:hi] = lst[lo:hi]
        i = lo
        j = mi
        k = lo
        while i < mi and j < hi:
            if buf[i] <= buf[j]:
                lst[k] = buf[i]
                i += 1
            else:
                lst[k] = buf[j]
                j += 1
            k += 1
        while i < mi:
            lst[k] = buf[i]
            i += 1
            k += 1
        while j < hi:
            lst[k] = buf[j]
            j += 1
            k += 1

    mergesort_(0, len(lst))


def mergesort_bottomup(lst):
    # NOTE: we can reduce the extra space to ``len(lst) // 2``
    buf = [None] * len(lst)
    step = 1
    while step < len(lst):
        # Invariant: lst[step*i:step*(i+1)] is already sorted for all valid i.
        for lo in range(0, len(lst) - step, step << 1):
            mi = lo + step
            hi = min(mi + step, len(lst))
            buf[lo:hi] = lst[lo:hi]
            i = k = lo
            j = mi
            while i < mi and j < hi:
                if buf[i] <= buf[j]:
                    lst[k] = buf[i]
                    i += 1
                else:
                    lst[k] = buf[j]
                    j += 1
                k += 1
            while i < mi:
                lst[k] = buf[i]
                i += 1
                k += 1
            while j < hi:
                lst[k] = buf[j]
                j += 1
                k += 1
        step <<= 1


def heapsort(lst):
    # NOTE: we use heap with 0-based indexes. So the left child of `i` is ``2*i + 1``.
    def push_down(i, lst_size):
        while True:
            child_index = 2*i + 1
            if child_index >= lst_size:
                return
            if child_index + 1 < lst_size and lst[child_index + 1] > lst[child_index]:
                child_index += 1
            if lst[child_index] > lst[i]:
                lst[i], lst[child_index] = lst[child_index], lst[i]
                i = child_index
            else:
                return
    

    # Heapify `lst`.
    for i in range(len(lst) // 2 - 1, -1, -1):
        push_down(i, len(lst))

    # Inplace sort.
    for last_element_index in range(len(lst) - 1, 0, -1):
        lst[0], lst[last_element_index] = lst[last_element_index], lst[0]
        push_down(0, last_element_index)



def test():
    random_state = random.getstate()
    random.seed(0)

    def check(func, lst):
        lst2 = sorted(lst)
        func(lst)
        assert lst == lst2

    sorting_functions = [
        obj
        for name, obj in globals().items()
        if 'sort' in name
    ]

    random_lists = []
    random_list_sizes = [randrange(0, 500) for _ in range(500)] + list(range(500))
    for size in random_list_sizes:
        size = randrange(0, 500)
        random_lists.append(
            [random.random() for _ in range(size)]
        )
        random_lists.append(
            [random.randrange(100) for _ in range(size)]
        )

    for func in sorting_functions:
        check(func, [])
        check(func, [1])
        check(func, [1,2,3])
        check(func, [3,2,1])
        check(func, [1]*100)
        check(func, list(range(100)))
        check(func, list(range(100, -100, -1)))
        for rlst in random_lists:
            check(func, rlst)

    random.setstate(random_state)


def benchmark():
    import timeit
    random_state = random.getstate()
    random.seed(0)


    sorting_functions = [
        (name, obj)
        for name, obj in globals().items()
        if 'sort' in name
    ]
    sorting_functions.sort()

    
    def test(name, lst):
        print('========== {} ========='.format(name))
        for name, func in sorting_functions:
            print('{}: {}'.format(name, timeit.timeit('func(lst)', globals=locals(), number=20)))


    SIZE = 900
    test('Random', [random.random() for _ in range(SIZE)])
    test('Sorted', list(range(SIZE)))
    test('Reversed', list(range(SIZE - 1, -1, -1)))
    test('All 1', [1] * SIZE)

    random.setstate(random_state)


if __name__ == "__main__":
    benchmark()
