class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        can_kill = [ [ [0] * 4  for _ in range(ncols) ] for _ in range(nrows)]
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 'E':
                    can_kill[row][col] = [1] * 4

        # Handle upward and leftward enemies
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] != 'W':
                    if row > 0:
                        can_kill[row][col][0] += can_kill[row-1][col][0]
                    if col > 0:
                        can_kill[row][col][1] += can_kill[row][col-1][1]

        # Handle downward and rightward enemies
        for row in range(nrows-1, -1, -1):
            for col in range(ncols-1, -1, -1):
                if grid[row][col] != 'W':
                    if row < nrows - 1:
                        can_kill[row][col][2] += can_kill[row+1][col][2]
                    if col < ncols - 1:
                        can_kill[row][col][3] += can_kill[row][col+1][3]

        maximum = 0
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == '0':
                    maximum = max(maximum, sum(can_kill[row][col]))

        return maximum


def test():
    def check(grid, expected):
        converted_grid = [
            list(line.strip())
            for line in grid.strip().splitlines()
        ]
        assert Solution().maxKilledEnemies(converted_grid) == expected

    check(
        """
        0E00
        E0WE
        0E00
        """, 3
    )
    check('', 0)
    check(
        """
        0EE0
        E0WE
        0E00
        """, 3
    )
    check(
        """
        E0EE
        E0WE
        0E00
        """, 4
    )
