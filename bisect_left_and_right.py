# This implement the bisect_left and bisect_right

def bisect_left(a, x):
    l = 0
    r = len(a) - 1
    while r >= l:
        m = (l + r) // 2
        if a[m] >= x:
            r = m - 1
        else:
            l = m + 1
    return l

def bisect_right(a, x):
    l = 0
    r = len(a) - 1
    while r >= l:
        m = (l + r) // 2
        if a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return l

def test():
    assert bisect_left([], 0) == 0
    assert bisect_right([], 0) == 0
    assert bisect_left([1], 0) == 0
    assert bisect_right([1], 0) == 0
    assert bisect_left([1], 1) == 0
    assert bisect_right([1], 1) == 1
    assert bisect_left([1], 2) == 1
    assert bisect_right([1], 2) == 1

    assert bisect_left([1,2,3,4,5], 0) == 0
    assert bisect_right([1,2,3,4,5], 0) == 0
    assert bisect_left([1,2,3,4,5], 1) == 0
    assert bisect_right([1,2,3,4,5], 1) == 1
    assert bisect_left([1,2,3,4,5], 1.5) == 1
    assert bisect_right([1,2,3,4,5], 1.5) == 1
    assert bisect_left([1,2,3,4,5], 2) == 1
    assert bisect_right([1,2,3,4,5], 2) == 2
    assert bisect_left([1,2,3,4,5], 5) == 4
    assert bisect_right([1,2,3,4,5], 5) == 5
    assert bisect_left([1,2,3,4,5], 6) == 5
    assert bisect_right([1,2,3,4,5], 6) == 5

    assert bisect_left([1,2,3,3,4,5], 3) == 2
    assert bisect_right([1,2,3,3,4,5], 3) == 4
    assert bisect_left([1,2,3,3,3,4,5], 3) == 2
    assert bisect_right([1,2,3,3,3,4,5], 3) == 5

def test_random():
    from bisect import bisect_left as bl, bisect_right as br
    import random
    
    for _ in range(500):
        array = [random.randint(1, 20) for _ in range(random.randint(1, 100))]
        array.sort()
        for _ in range(100):
            x = random.randint(-5, 25)
            assert bisect_left(array, x) == bl(array, x)
            assert bisect_right(array, x) == br(array, x)
