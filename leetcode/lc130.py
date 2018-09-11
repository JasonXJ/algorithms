class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        nrow = len(board)
        if nrow == 0:
            return
        ncol = len(board[0])
        if ncol == 0:
            return

        def recursive_mark(r, c):
            if 0 <= r < nrow and 0 <= c < ncol and board[r][c] == 'O':
                board[r][c] = 'o'
                recursive_mark(r-1, c)
                recursive_mark(r, c-1)
                recursive_mark(r+1, c)
                recursive_mark(r, c+1)

        for c in range(ncol):
            recursive_mark(0, c)
            if nrow != 1:
                recursive_mark(nrow-1, c)
        for r in range(1, nrow-1):
            recursive_mark(r, 0)
            if ncol != 1:
                recursive_mark(r, ncol-1)
        
        for row in board:
            for c in range(ncol):
                if row[c] == 'o':
                    row[c] = 'O'
                elif row[c] == 'O':
                    row[c] = 'X'
