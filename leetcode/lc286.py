# An O(mn) solution using BFS
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647

        if len(rooms) == 0 or len(rooms[0]) == 0:
            return

        nrows = len(rooms)
        ncols = len(rooms[0])
        
        locations = [
            (row, col)
            for row in range(nrows)
            for col in range(ncols)
            if rooms[row][col] == 0
        ]
        next_locations = []
        next_distance = 1

        while locations:
            for row, col in locations:
                neighbours = (
                    (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
                )
                for row2, col2 in neighbours:
                    if (0 <= row2 < nrows and
                            0 <= col2 < ncols and
                            rooms[row2][col2] == INF):
                        rooms[row2][col2] = next_distance
                        next_locations.append((row2, col2))
            locations, next_locations = next_locations, []
            next_distance += 1
