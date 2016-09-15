# An O(min(m, n)*lg(max(m, n))) solution
class Solution(object):
    class MatrixProxy:
        def __init__(self, matrix):
            self.matrix = matrix
            self._real_nrows = len(matrix)
            self._real_ncols = len(matrix[0])
            if self._real_nrows > self._real_ncols:
                self.nrows, self.ncols = self._real_ncols, self._real_nrows
                self.get_value = lambda row, col: self.matrix[col][row]
            else:
                self.nrows, self.ncols = self._real_nrows, self._real_ncols
                self.get_value = lambda row, col: self.matrix[row][col]

    
    @staticmethod
    def bisect(value_getter, li, hi, target):
        while li <= hi:
            mi = (li + hi) // 2
            value = value_getter(mi)
            if value == target:
                return True, mi
            elif value < target:
                li = mi + 1
            else:
                hi = mi - 1

        return False, li


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        matrix_proxy = self.MatrixProxy(matrix)
        last_column = matrix_proxy.ncols - 1
        
        # Identifing rows which might contain the target
        found, row_end = self.bisect(lambda row:matrix_proxy.get_value(row, 0),
                              0, matrix_proxy.nrows - 1, target)
        if found:
            return True
        found, row_start = self.bisect(lambda row:matrix_proxy.get_value(row, last_column),
                                0, matrix_proxy.nrows - 1, target)
        if found:
            return True
        
        # Binarily search rows [row_start, row_end)
        for row in range(row_start, row_end):
            found, _ = self.bisect(lambda col:matrix_proxy.get_value(row, col),
                                0, last_column, target)
            if found:
                return True

        return False


# This is an O(m + n) algorithm. See
# https://discuss.leetcode.com/topic/20064/my-concise-o-m-n-java-solution
class Solution2(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        nrows = len(matrix)
        ncols = len(matrix[0])
        # Start from the top right corner
        row, col = 0, ncols - 1
        while row < nrows and col >= 0:
            different = matrix[row][col] - target
            if different == 0:
                return True
            elif different > 0:
                # We can rule out the current column.
                col -= 1
            else:
                # We can rule out the current row.
                row += 1

        return False
        

def test():
    for S in (Solution, Solution2):
        matrix1 = [
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        assert S().searchMatrix(matrix1, -100) == False
        assert S().searchMatrix(matrix1, 100) == False
        assert S().searchMatrix(matrix1, 5) == True
        assert S().searchMatrix(matrix1, 20) == False
        assert S().searchMatrix(matrix1, 1) == True
        assert S().searchMatrix(matrix1, 18) == True
        assert S().searchMatrix(matrix1, 15) == True
        assert S().searchMatrix(matrix1, 30) == True
        assert S().searchMatrix(matrix1, 26) == True
        assert S().searchMatrix(matrix1, 27) == False

        matrix2 = [
            [1,   4,  7, 11],
            [2,   5,  8, 12],
            [3,   6,  9, 16],
            [10, 13, 14, 17],
            [18, 21, 23, 26]
        ]
        assert S().searchMatrix(matrix2, -100) == False
        assert S().searchMatrix(matrix2, 100) == False
        assert S().searchMatrix(matrix2, 5) == True
        assert S().searchMatrix(matrix2, 20) == False
        assert S().searchMatrix(matrix2, 1) == True
        assert S().searchMatrix(matrix2, 18) == True
        assert S().searchMatrix(matrix2, 15) == False
        assert S().searchMatrix(matrix2, 30) == False
        assert S().searchMatrix(matrix2, 26) == True
        assert S().searchMatrix(matrix2, 27) == False

        row_matrix = [[1,3,5,7,9]]
        col_matrix = [[1], [3], [5], [7], [9]]
        for matrix3 in (row_matrix, col_matrix):
            for x in range(10):
                assert S().searchMatrix(matrix3, x) == ((x & 1) == 1)
