# O(n^3) solution.
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # matrix[i][j] is the minimal amount of money to guarantee a win when
        # the range of number to guess is [1, n]. Note that we has an extra row
        # at the bottom and we initialize all the values to 0, which make sure
        # that the DP process executes correctly.
        matrix = [[0] * (n + 1) for _ in range(n+2)]

        # Fill the matrix from bottom to top, from left to right.
        for i in range(n, 0, -1):
            for j in range(i + 1, n + 1):
                matrix[i][j] = min(
                    r + max(matrix[i][r-1], matrix[r+1][j])
                    for r in range(i, j + 1)
                )

        return matrix[1][n]


def test():
    assert Solution().getMoneyAmount(1) == 0
    assert Solution().getMoneyAmount(2) == 1
    assert Solution().getMoneyAmount(3) == 2
    assert Solution().getMoneyAmount(4) == 4
    assert Solution().getMoneyAmount(5) == 6
    assert Solution().getMoneyAmount(7) == 10
