# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l < h:
            m = (l + h) // 2
            guess_rv = guess(m)
            if guess_rv == 0:
                return m
            if guess_rv == -1:
                h = m - 1
            else:
                l = m + 1

        return l
