class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while True:
            if n & 1:
                if n == 1:
                    return True
                else:
                    return False
            n >>= 1
