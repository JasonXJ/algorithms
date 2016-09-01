# An O(mn) time and O(1) space solution (Note that strictly speaking, since I
# used :func:`range`, which use linear space in python2, so the used space is
# actually larger than O(1))
class Solution(object):
    def setZeroes(self, matrix):
        columns = len(matrix[0])
        first_row_with_0 = None
        for row_no, row in enumerate(matrix):
            if 0 in row:
                first_row_with_0_no = row_no
                first_row_with_0 = row
                break
        if first_row_with_0 is None:
            return
        
        for row_no in range(first_row_with_0_no+1, len(matrix)):
            zero_found = False
            row = matrix[row_no]
            for col_no in range(columns):
                if row[col_no] == 0:
                    zero_found = True
                    first_row_with_0[col_no] = 0
            if zero_found:
                for col_no in range(columns):
                    row[col_no] = 0

        # Set columns
        for col_no in range(columns):
            if first_row_with_0[col_no] == 0:
                for row_no in range(len(matrix)):
                    matrix[row_no][col_no] = 0
            else:
                first_row_with_0[col_no] = 0

if __name__ == "__main__":
    print(Solution().setZeroes([[0],[1]]))
