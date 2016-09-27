class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(t) == 0:
            return 1
        if len(s) == 0:
            return 0

        memo = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for row in range(len(s) + 1):
            memo[row][0] = 1

        for row in range(1, len(s) + 1):
            for col in range(1, len(t) + 1):
                memo[row][col] = memo[row-1][col]
                if s[row - 1] == t[col - 1]:
                    memo[row][col] += memo[row-1][col-1]
        
        return memo[len(s)][len(t)]
