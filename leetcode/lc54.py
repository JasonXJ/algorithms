class Solution(object):
    def spiralOrder(self, matrix):
        rv = []
        rows = len(matrix)
        if rows == 0:
            return []
        cols = len(matrix[0])
        top = 0
        bottom = rows
        left = -1
        right = cols

        row = 0
        col = -1
        while True:
            # Go right
            col += 1
            if col == right:
                break
            while col != right:
                rv.append(matrix[row][col])
                col += 1
            col -= 1
            right -= 1

            # Go down
            row += 1
            if row == bottom:
                break
            while row != bottom:
                rv.append(matrix[row][col])
                row += 1
            row -= 1
            bottom -= 1

            # Go left
            col -= 1
            if col == left:
                break
            while col != left:
                rv.append(matrix[row][col])
                col -= 1
            col += 1
            left += 1

            # Go up
            row -= 1
            if row == top:
                break
            while row != top:
                rv.append(matrix[row][col])
                row -= 1
            row += 1
            top += 1

        return rv

if __name__ == "__main__":
    print(
        Solution().spiralOrder(
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    ))
