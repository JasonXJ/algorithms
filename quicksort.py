def quicksort(array):
    def partition(begin, end):
        pivot_value = array[end-1]
        i = j = begin
        while j < end:
            if array[j] < pivot_value:
                array[i], array[j] = array[j], array[i]
                i += 1
            j += 1
        array[i], array[end-1] = array[end-1], array[i]
        return i

    def inner(begin, end):
        if end <= begin:
            return
        k = partition(begin, end)
        inner(begin, k)
        inner(k+1, end)

    inner(0, len(array))

def _check(array):
    quicksort(array)
    assert array == sorted(array)

def test():
    _check([])
    _check([1])
    _check([1,2])
    _check([2,1])
    _check([2,2])
    _check([1,2,3,4])
    _check([4,3,2,1])

    import random
    for _ in range(500):
        array = [random.randint(1, 20) for _ in range(random.randint(1, 100))]
        _check(array)
