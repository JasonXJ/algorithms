class Solution(object):
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        # First row
        first_row = grid[0]
        for col in range(1, cols):
            first_row[col] += first_row[col-1]

        # First column
        for row in range(1, rows):
            grid[row][0] += grid[row-1][0]

        for row in range(1, rows):
            for col in range(1, cols):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])

        return grid[-1][-1]
