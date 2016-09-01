def contiguous_max_sum(array):
    # This initialization is OK even if the array only contains negative
    # values. Because the size of contiguous sequence can be zero and the sum
    # should be 0.
    max_sum = 0

    current_sum = 0 # It should never drop below 0
    for x in array:
        if x >= 0: # Still increasing (or not changing)
            current_sum += x
        else: # x < 0, decrasing
            # Check if it is already larger than max_sum
            if current_sum > max_sum:
                max_sum = current_sum

            current_sum += x
            if current_sum < 0:
                # Restart the sequence, which means that we reset current_sum to 0
                current_sum = 0

    # FIXME: Check `current_sum > max_sum` again here
    if current_sum > max_sum:
        max_sum = current_sum

    return max_sum

def test_contiguous_max_sum():
    # Special cases
    assert contiguous_max_sum([]) == 0
    assert contiguous_max_sum([-1, -2, -3, -1, -2, -4, -100]) == 0

    # The sequence continues to the end
    assert contiguous_max_sum([1, -2, 2, 3, 4]) == 9

    assert contiguous_max_sum([1, 2, -2, 2, 3, 4]) == 10
    assert contiguous_max_sum([1, 2, -2, -1, 3, 4]) == 7
    assert contiguous_max_sum([-1, -2, 2, 1, -3, -4]) == 3
    assert contiguous_max_sum([-1, 2, 1, -3, -4, 2, 3, -100, 2]) == 5
