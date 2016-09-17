from heapq import heappush, heappop
# O(k log k) solution.
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        assert k >= 1
        if k == 1:
            return matrix[0][0]
        nrows = len(matrix)
        ncols = len(matrix[0])
        visited = {(0, 0)}
        heap = [(matrix[0][0], 0, 0)]
        discarded = 0
        
        while discarded != k - 1:
            _, row, col = heappop(heap)
            discarded += 1
            if row + 1 < nrows and (row + 1, col) not in visited:
                heappush(heap, (matrix[row+1][col], row + 1, col))
                visited.add((row + 1, col))
            if col + 1 < ncols and (row, col + 1) not in visited:
                heappush(heap, (matrix[row][col+1], row, col + 1))
                visited.add((row, col + 1))

        return heap[0][0]
