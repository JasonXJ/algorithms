class Solution(object):
    def searchMatrix(self, matrix, target):
        # Search rows
        l = 0
        h = len(matrix) - 1
        while l <= h:
            mid = (l + h) // 2
            v = matrix[mid][0]
            if v == target:
                return True
            elif v > target:
                h = mid - 1
            else:
                l = mid + 1
        if h != -1:
            row = matrix[h]
            l2 = 0
            h2 = len(row) - 1
            while l2 <= h2:
                mid = (l2 + h2) // 2
                v = row[mid]
                if v == target:
                    return True
                elif v > target:
                    h2 = mid - 1
                else:
                    l2 = mid + 1

        return False

def test():
    matrix = [ [1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50] ]
    func = Solution().searchMatrix

    assert func(matrix, 1)
    assert func(matrix, 3)
    assert func(matrix, 10)
    assert func(matrix, 20)
    assert func(matrix, 50)
    assert not func(matrix, 60)
    assert not func(matrix, -1)
