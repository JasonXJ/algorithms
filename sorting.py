import random

def quicksort(A):
    def recursive_quicksort(f, l):
        if f < l:
            p = partition(f, l)
            recursive_quicksort(f, p-1)
            recursive_quicksort(p+1, l)

    def partition(f, l):
        i = f-1
        x = A[l]
        for j in range(f, l):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        i += 1
        A[i], A[l] = A[l], A[i]
        return i

    recursive_quicksort(0, len(A)-1)

def mergesort(A):
    # Only need the size of floor(len(A) / 2)
    temp_buf = [0 for x in range(len(A)//2)]

    def recursive_mergesort(begin, end):
        if begin+1 < end:
            mid = (begin + end) // 2
            recursive_mergesort(begin, mid)
            recursive_mergesort(mid, end)
            
            # Copy the first half to temp_buf
            temp_buf[:mid-begin] = A[begin:mid]

            # Merge temp_buf with the second half and store the result in
            # A[begin...end].
            i1 = 0
            i1_end = mid-begin
            i2 = mid
            i2_end = end
            j = begin
            while i1 < i1_end and i2 < i2_end:
                if temp_buf[i1] <= A[i2]:
                    A[j] = temp_buf[i1]
                    i1 += 1
                else:
                    A[j] = A[i2]
                    i2 += 1
                j += 1

            # If i1 < i1_end, we need to copy the remain elements in
            # `temp_buf`. However, if it is i2 < i2_end, we need not do
            # anything because the remain elements are already at the proper
            # places of array `A`
            if i1 < i1_end:
                assert end - j == i1_end - i1
                A[j:end] = temp_buf[i1:i1_end]

    recursive_mergesort(0, len(A))
    assert len(temp_buf) == len(A)//2

def _sorting_test(sorting_functions, times=100, array_size=100, element_range=(0, 50)):
    for _ in range(times):
        array = [random.randint(*element_range) for _ in range(array_size)]
        true_result = sorted(array)
        for func in sorting_functions:
            temp_array = array[:]
            func(temp_array)
            assert temp_array == true_result

def test_quicksort():
    _sorting_test([quicksort])


def test_quicksort():
    _sorting_test([mergesort])
