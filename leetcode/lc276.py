class Solution(object):
    """ 
    This solution uses a little math. Let's denote the number of pairs of
    consecutive posts painted with the same color by b and the number of other
    posts by a. Thus, a + 2b = n (or a = n - 2b). The range of b is [0, n //
    2]. Then, the ways equal::

        sum(combination((n-2b)+b, b) * k * (k-1) ** ((n-2b)+b-1) for b in range(n//2 + 1))

    By calculate each of item to be sum **incrementally**, we have the
    following code.
    """
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        if k == 1:
            if n == 1 or n == 2:
                return 1
            else:
                return 0

        b_upper = n // 2
        rv = 0
        # Initial `g` to "g(0)"
        g = k * (k - 1) ** (n - 0 - 1)
        rv += g
        for b in range(1, b_upper + 1):
            # Note that we must first do the multiplication and then the
            # integer division, otherwise the result might be wrong due to
            # precision lost brought by the integer division.
            g *= (n - 2*b + 2) * (n - 2*b + 1)
            g //= (n - (b - 1)) * b * (k - 1)
            rv += g
        
        return rv


def g(n, k, b):
    from math import factorial
    return factorial(n-b) / factorial(b) / factorial(n - 2*b) * (k * (k - 1) ** (n - b - 1))


def test():
    assert Solution().numWays(100, 1) == 0
    assert Solution().numWays(3, 3) == 24
    assert Solution().numWays(4, 3) == 66
    assert Solution().numWays(5, 3) == 180
