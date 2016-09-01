class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) <= 1:
            return

        for row in range(len(matrix) // 2):
            for col in range((len(matrix) + 1) // 2):
                value = matrix[row][col]
                for _ in range(4):
                    row, col = col, len(matrix) - 1 - row
                    value, matrix[row][col] = matrix[row][col], value


def test(matrix, expected_result):
    print(matrix)
    Solution().rotate(matrix)
    print(matrix)
    assert matrix == expected_result


if __name__ == "__main__":
    test(
        [[1,2],[3,4]],
        [[3,1],[4,2]],
    )
    test(
        [[1,2,3],[8,9,4],[7,6,5]],
        [[7,8,1],[6,9,2],[5,4,3]],
    )
