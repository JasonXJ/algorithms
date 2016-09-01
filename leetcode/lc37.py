# Note that I use unicode instead of str so that the code can pass leetcode
# online judge.

class Solution(object):
    def solveSudoku(self, board):
        self.finished = False
        self._preprocessBoard(board)
        self._solveSudoku(board)
        assert self.finished

    @classmethod
    def _preprocessBoard(cls, board):
        # Replace all '.' with a list of candidates.
        # XXX: this is not an efficient algorithm
        init_cell = [unicode(x) for x in range(1, 10)]
        for row in range(9):
            for col in range(9):
                if board[row][col] == u'.':
                    board[row][col] = init_cell[:]
        for row in range(9):
            for col in range(9):
                if isinstance(board[row][col], unicode):
                    if cls._updateRestriction(board, row, col) == False:
                        raise ValueError

    def _solveSudoku(self, board):
        # First, find the most restricted candidate cell.
        min_num_candidates = 10
        min_row = min_col = None
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if isinstance(cell, list):
                    if len(cell) < min_num_candidates:
                        min_num_candidates = len(cell)
                        min_row = row
                        min_col = col
        if min_row is None:
            self.finished = True
            return

        # Start searching
        candidates = board[min_row][min_col]
        for x in candidates:
            board[min_row][min_col] = x
            
            # Update restrictions
            updated_coordinates = self._updateRestriction(board, min_row, min_col)
            if updated_coordinates == False:  # Failed to update restriction
                continue

            # Solve the subproblem
            self._solveSudoku(board)
            if self.finished:
                return

            # Failed. Do some recovery.
            self._recoverBoard(board, updated_coordinates, x)

        # All failed, recover and return.
        board[min_row][min_col] = candidates

        return

    @staticmethod
    def _recoverBoard(board, coordinates, value):
        for row, col in coordinates:
            board[row][col].append(value)

    @classmethod
    def _updateRestriction(cls, board, row, col):
        updated_coordinates = []
        value = board[row][col]
        assert isinstance(value, unicode)

        def updateCellOrRecover(row, col):
            cell = board[row][col]
            if isinstance(cell, list):
                try:
                    index = cell.index(value)
                except ValueError:
                    pass
                else:
                    # Remove cell[index]
                    cell[index] = cell[-1]
                    del cell[-1]
                    updated_coordinates.append((row, col))

                    if len(cell) == 0:
                        # Dead end. Recover and return False.
                        cls._recoverBoard(board, updated_coordinates, value)
                        return False

        # update the row and columns
        for x in range(9):
            if (updateCellOrRecover(x, col) == False) or (updateCellOrRecover(row, x) == False):
                return False
        
        # update the small matrix
        row_start = row//3*3
        col_start = col//3*3
        for temp_row in range(row_start, row_start+3):
            for temp_col in range(col_start, col_start+3):
                if updateCellOrRecover(temp_row, temp_col) == False:
                    return False

        return updated_coordinates
