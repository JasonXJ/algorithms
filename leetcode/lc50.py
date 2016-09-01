class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1. / x
            n = -n
        rv = 1
        while n != 0:
            if n & 0x1:
                rv *= x
            x *= x
            n >>= 1
        return rv

def test():
    func = Solution().myPow
    assert func(100, 0) == 1
    assert func(1, 10) == 1
    assert func(2, 1) == 2
    assert func(2, 2) == 4
    assert func(2, 7) == 2**7
    assert func(3, 13) == 3**13
    assert func(3, 8) == 3**8
