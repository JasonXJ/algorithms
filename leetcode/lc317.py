class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        nrows = len(grid)
        ncols = len(grid[0])
        distance_grid = [[0] * ncols for _ in range(nrows)]
        visited_grid = [[0] * ncols for _ in range(nrows)]
        self.building_processed = 0

        def process_new_building(row, col):
            current_nodes = [(row, col)]
            next_nodes = []
            next_distance = 1
            while current_nodes:
                for row2, col2 in current_nodes:
                    neighbours = (
                        (row2 - 1, col2),
                        (row2 + 1, col2),
                        (row2, col2 - 1),
                        (row2, col2 + 1)
                    )
                    for row3, col3 in neighbours:
                        if (0 <= row3 < nrows and
                                0 <= col3 < ncols and
                                grid[row3][col3] == 0 and
                                visited_grid[row3][col3] == self.building_processed):
                            next_nodes.append((row3, col3))
                            visited_grid[row3][col3] += 1
                            distance_grid[row3][col3] += next_distance

                current_nodes, next_nodes = next_nodes, []
                next_distance += 1
            self.building_processed += 1

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 1:
                    process_new_building(row, col)

        if self.building_processed == 0:
            if any(grid[row][col] == 0 for row in range(nrows) for col in range(ncols)):
                return 0
            else:
                return -1

        minimum_distance = float('+inf')
        for row in range(nrows):
            for col in range(ncols):
                if visited_grid[row][col] == self.building_processed:
                    minimum_distance = min(minimum_distance, distance_grid[row][col])

        if minimum_distance == float('+inf'):
            return -1
        return minimum_distance
                    

def test():
    assert Solution().shortestDistance([
        [1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0],
    ]) == 7
    assert Solution().shortestDistance([
        [1,2,2,0,1],
        [2,0,0,0,0],
        [0,0,1,0,0],
    ]) == -1
    assert Solution().shortestDistance([
        [0,2,2,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]) == 0
    assert Solution().shortestDistance([
        [1,2,2,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]) == 1
    assert Solution().shortestDistance([
        [1,2,2,0,0],
        [1,0,0,0,0],
        [0,0,0,0,0],
    ]) == -1
    assert Solution().shortestDistance([
        [1,2,2,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
    ]) == -1
