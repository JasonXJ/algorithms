class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        nrows = len(board)
        ncols = len(board[0])
        for row in range(nrows):
            for col in range(ncols):
                alive_neighbors = 0
                for row2 in (row - 1, row, row + 1):
                    if 0 <= row2 < nrows:
                        for col2 in (col - 1, col, col + 1):
                            if 0 <= col2 < ncols:
                                if board[row2][col2] & 1:
                                    alive_neighbors += 1
                # Note that for the current node, there is no need to use the
                # mask `1`.
                alive_neighbors -= board[row][col]
                if alive_neighbors == 3 or (alive_neighbors == 2 and board[row][col]):
                    board[row][col] |= 0b10

        for row in range(nrows):
            for col in range(ncols):
                board[row][col] >>= 1


def test():
    def subtest(board, expected):
        Solution().gameOfLife(board)
        assert board == expected

    subtest([[1,1,1],[1,1,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]])
