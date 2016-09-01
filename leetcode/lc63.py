class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        assert len(obstacleGrid) > 0 and len(obstacleGrid[0]) > 0
        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])
        paths = [[0]*ncols for _ in range(nrows)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            paths[0][0] = 1

        # Init first row
        first_row = paths[0]
        input_first_row = obstacleGrid[0]
        for i in range(1, ncols):
            if input_first_row[i] == 1:
                break
            first_row[i] = 1

        # Init first col
        for i in range(1, nrows):
            if obstacleGrid[i][0] == 1:
                break
            paths[i][0] = 1

        for rowi in range(1, nrows):
            for coli in range(1, ncols):
                if obstacleGrid[rowi][coli] != 1:
                    paths[rowi][coli] = paths[rowi-1][coli] + paths[rowi][coli-1]

        return paths[nrows-1][ncols-1]

if __name__ == "__main__":
    f = Solution().uniquePathsWithObstacles
    assert 2 == f([
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ])
    assert 0 == f([[1]])
    assert 1 == f([[0]])
    assert 0 == f([
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ])

