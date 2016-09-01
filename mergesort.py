def mergesort(array):
    def merge(destination, array1, array2):
        index = 0
        index1 = 0
        index2 = 0
        while index1 < len(array1) and index2 < len(array2):
            if array1[index1] <= array2[index2]:
                destination[index] = array1[index1]
                index1 += 1
            else:
                destination[index] = array2[index2]
                index2 += 1
            index += 1
        while index1 < len(array1):
            destination[index] = array1[index1]
            index += 1
            index1 += 1
        while index2 < len(array2):
            destination[index] = array2[index2]
            index += 1
            index2 += 1

    def recursive(array):
        if len(array) <= 1:
            return
        mid = len(array) // 2
        array1 = array[:mid]
        array2 = array[mid:]
        recursive(array1)
        recursive(array2)
        merge(array, array1, array2)

    recursive(array)

def _check(array):
    mergesort(array)
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
