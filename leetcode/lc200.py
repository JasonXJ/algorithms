class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        visited = [[False]*ncols for _ in range(nrows)]

        def dfs(row_index, col_index):
            if (not (0 <= row_index < nrows) or
                    not (0 <= col_index < ncols) or
                    grid[row_index][col_index] == '0' or
                    visited[row_index][col_index] == True):
                return False
            visited[row_index][col_index] = True
            dfs(row_index+1, col_index)
            dfs(row_index-1, col_index)
            dfs(row_index, col_index+1)
            dfs(row_index, col_index-1)

            return True


        island = 0
        for row_index in range(nrows):
            for col_index in range(ncols):
                if dfs(row_index, col_index):
                    island += 1

        return island


def test():
    assert 1 == Solution().numIslands(
        [
            '11110',
            '11010',
            '11000',
            '00000',
        ]
    )
    assert 3 == Solution().numIslands(
        [
            '11000',
            '11000',
            '00100',
            '00011',
        ]
    )
    assert 1 == Solution().numIslands(
        [
            '11000',
            '11010',
            '01110',
            '10011',
            '10011',
            '11111',
        ]
    )

if __name__ == "__main__":
    import ipdb
    ipdb.set_trace()
    test()
