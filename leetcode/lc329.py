# An DP solution. Note that the general longest path problem cannot be solved
# by DP. However, in this case, since the path must be a strictly increasing
# path, the longest path of a neighour who has a larger value will not be
# overlapped with the path of the current cell. Thus, DP can be used.
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        longest = [[None] * ncols for _ in range(nrows)]


        def search(row=0, col=0):
            if 0 <= row < nrows and 0 <= col < ncols:
                if longest[row][col] is not None:
                    return longest[row][col]
                current_value = matrix[row][col]
                current_longest = 0
                for row2, col2 in ((row - 1, col),
                                   (row + 1, col),
                                   (row, col - 1),
                                   (row, col + 1)):
                    if (0 <= row2 < nrows and 0 <= col2 < ncols and
                            current_value < matrix[row2][col2]):
                        current_longest = max(current_longest, search(row2, col2))
                current_longest += 1
                longest[row][col] = current_longest
                return current_longest

            return 0

        
        for row in range(nrows):
            for col in range(ncols):
                if longest[row][col] is None:
                    search(row, col)
        return max(max(row) for row in longest)


def test():
    assert Solution().longestIncreasingPath([
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]) == 4
    assert Solution().longestIncreasingPath([
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ]) == 4
