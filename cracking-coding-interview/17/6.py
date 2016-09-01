def max_insert_index(value, array, start, end):
    # TODO: update to binary search
    # XXX: See the difference (`while` and `for` with break) between
    # `max_insert_index` and `min_insert_index`, that is something we need to
    # notice.
    i = start
    while i < end:
        if value < array[i]:
            break
        i += 1
    return i

def min_insert_index(value, array, start, end):
    # TODO: update to binary search
    for i in range(start, end):
        if value <= array[i]:
            break;
    else:
        return end
    return i

def required_sorting_subarray(array):
    """ This function returns a tuple ``(m, n)`` that if ``array[m:n]`` is
    sorted, than the whole array is sorted. Or returns None if it is already
    sorted  """
    
    if len(array) <= 1:
        return

    # Find the `left_boundary`, which is the largest value that makes
    # array[:left_boundry] sorted.
    for left_boundary in range(1, len(array)):
        if array[left_boundary-1] > array[left_boundary]:
            break
    else: # No break at all, the array is sorted.
        return None

    # Find the `right_boundary`, which is the smallest value that makes
    # array[right_boundary:] sorted. (Note that the for loop do not consider
    # right_boundary == 0, because we already know that `array` is not sorted.
    for right_boundary in range(len(array)-1, 0, -1):
        if array[right_boundary-1] > array[right_boundary]:
            break
    else:
        assert False, "Impossible"
    
    # Find the largest element in ``array[:right_boundary]``
    left_max = max(array[left_boundary-1:right_boundary])

    # Find the smallest element in ``array[left_boundary:]``
    right_min = min(array[left_boundary:right_boundary+1])

    m = max_insert_index(right_min, array, 0, left_boundary)
    n = min_insert_index(left_max, array, right_boundary, len(array))

    return (m, n)

def test_required_sorting_subarray():
    # Special cases
    assert required_sorting_subarray([]) is None
    assert required_sorting_subarray([10]) is None
    assert required_sorting_subarray([1,2,3,4,5,10]) is None

    # Boundaries overlapped
    assert required_sorting_subarray([1,2,3,1,2,3]) == (1, 5)
    assert required_sorting_subarray([4,5,6,1,2,3]) == (0, 6)
    assert required_sorting_subarray([4,5,6,1,2,6]) == (0, 5)
    assert required_sorting_subarray([1,5,6,1,2,3]) == (1, 6)

    # Boundaries not overlapped
    assert required_sorting_subarray([7,8,9,2,1,3,4,5,6]) == (0, 9)
    assert required_sorting_subarray([7,8,9,2,1,3,4,5,11]) == (0, 8)
    assert required_sorting_subarray([0,8,9,2,1,3,4,5,6]) == (1, 9)
    assert required_sorting_subarray([0,1,9,2,1,3,4,9,11]) == (2, 7)

    # Test if m/n is the largest/smallest one
    assert required_sorting_subarray([1,2,2,2,3,3,2]) == (4, 7)
    assert required_sorting_subarray([1,9,8,8,9,9,9]) == (1, 4)
