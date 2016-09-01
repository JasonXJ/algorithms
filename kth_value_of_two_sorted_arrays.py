def kth(a1, a2, k):
    """ return the kth smallest number in sorted array `a1` and `a2`. Note that
    the `k` is 1-based (so the range of k is [1, len(a1)+len(a2)]) """

    def safe_get_value(a, index):
        if index < 0:
            return float('-inf')
        elif index >= len(a):
            return float('+inf')
        return a[index]

    if not (1 <= k <= len(a1) + len(a2)):
        raise ValueError
    # Make sure a1 has smaller length
    if len(a1) > len(a2):
        a1, a2 = a2, a1

    low = 0
    if k > len(a1):
        high = len(a1) + 1
    else:
        high = k + 1

    while True:
        # "contribution" is the number of (smallest) elements taken from an
        # array to form the k smallest numbers. The contribution from array
        # `a1` (i.e. `contribution1) should be in the range of [low, high).

        assert high > low
        contribution1 = (low + high) // 2
        contribution2 = k - contribution1
        if safe_get_value(a1, contribution1) < safe_get_value(a2, contribution2-1):
            # Need to let a1 contributes more.
            low = contribution1 
        elif safe_get_value(a2, contribution2) < safe_get_value(a1, contribution1-1):
            # Need to make a2 contributes more, i.e., make a1 contributes less.
            high = contribution1
        else:  # Balanced
            break

    return max(safe_get_value(a1, contribution1-1), safe_get_value(a2, contribution2-1))


def test_kth():
    import random
    for _ in range(1000):
        size = random.randint(1, 50)
        a1 = []
        a2 = []
        for i in range(size):
            random.choice((a1, a2)).append(i)
        for k in range(1, size+1):
            assert kth(a1, a2, k) == k - 1
