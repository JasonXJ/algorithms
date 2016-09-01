class Solution(object):
    def uniquePaths(self, m, n):
        grid = [[1]*n]
        for _ in range(m-1):
            grid.append([None]*n)
        for row in range(1, m):
            for col in range(n):
                # print(grid)
                ways = 0
                ways += grid[row-1][col]
                if col > 0:
                    ways += grid[row][col-1]
                grid[row][col] = ways
        return grid[m-1][n-1]

if __name__ == "__main__":
    print(Solution().uniquePaths(19, 13))
