class ColumnProxy:
    def __init__(self, a, column):
        self.a = a
        self.column = column

    def __getitem__(self, row):
        return self.a[row][self.column]

    def __len__(self):
        return len(self.a)

class RowProxy:
    def __init__(self, a, row):
        self.a = a
        self.row = row

    def __getitem__(self, column):
        return self.a[self.row][column]

    def __len__(self):
        return len(self.a[self.row])

def binary_search(a, x):
    b = 0
    e = len(a)
    while b < e:
        mid = (b+e)//2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            e = mid
        else:
            b = mid + 1
    return b

def matrix_search(matrix, val):
    rows = len(matrix)
    columns = len(matrix[0])

    # Calculate `candidate_row_upper_bound`. The corresponding row is the first
    # row (i.e. has smallest row index) that the value of its first column is
    # larger than val.
    candidate_row_upper_bound = binary_search(ColumnProxy(matrix, 0), val)
    if candidate_row_upper_bound < rows and matrix[candidate_row_upper_bound][0] == val:
        # Already find the val, return now
        return candidate_row_upper_bound, 0
    if candidate_row_upper_bound == 0:
        # All values are larger than val
        return None

    # Calculate `candidate_row_lower_bound`. The corresponding row is the last
    # one (i.e. has the largest index) that the value of its last column is
    # smaller than val.
    insert_point = binary_search(ColumnProxy(matrix, columns-1), val)
    if insert_point < rows and matrix[insert_point][columns-1] == val:
        # Already find the val, return now
        return insert_point, columns-1
    candidate_row_lower_bound = insert_point - 1

    for row in range(candidate_row_lower_bound+1, candidate_row_upper_bound):
        index = binary_search(RowProxy(matrix, row), val)
        if matrix[row][index] == val:
            return row, index

def test_binary_search():
    assert binary_search([1,2,3,4,5], 3) == 2
    assert binary_search([1,2,4,4,5], 3) == 2
    assert binary_search([1,2,3,4,5,6], 3) == 2
    assert binary_search([1,2,4,4,5,6], 3) == 2

def test_matrix_search():
    def subtest(matrix, val, expect_None=False):
        rv = matrix_search(matrix, val)
        if rv is None:
            assert expect_None
        else:
            row, column = rv
            assert matrix[row][column] == val

    matrix1 = [
        [1, 2, 3, 4],
        [5, 8, 9, 10],
        [6, 7, 9, 10],
        [11, 12, 13, 14],
    ]
    # Corner and edge cases
    subtest(matrix1, 1)
    subtest(matrix1, 4)
    subtest(matrix1, 5)
    subtest(matrix1, 10)
    subtest(matrix1, 11)
    subtest(matrix1, 14)

    # Others
    subtest(matrix1, 8)
    subtest(matrix1, 9)
    subtest(matrix1, 7)

    # Extreme
    subtest(matrix1, 20, True)
    subtest(matrix1, 0, True)
