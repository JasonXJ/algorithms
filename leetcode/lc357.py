class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n > 10:
            n = 10
        x = 11 - n
        c = 1
        while x <= 9:
            c = c * x + 1
            x += 1
        c -= 1

        return 10 + 9*c
