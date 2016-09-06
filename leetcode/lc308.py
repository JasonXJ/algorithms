class NumMatrix(object):

    class TwoDTree(object):
        class Node(object):
            def __init__(self, index, is_row_node):
                self.index = index
                self.left = None
                self.right = None
                if is_row_node:
                    # Only for row nodes
                    self.col_tree = None
                else:
                    # Only for column nodes
                    self.left_and_self_weight = 0


        def __init__(self, matrix):
            assert len(matrix) > 0 and len(matrix[0]) > 0
            self.nrows = len(matrix)
            self.ncols = len(matrix[0])
            self.current_values = [[0] * self.ncols for _ in range(self.nrows)]

            def build_tree():
                def build_col_trees(row_tree_node):
                    if row_tree_node is None:
                        return
                    row_tree_node.col_tree = self._build(0, self.ncols - 1, False)
                    build_col_trees(row_tree_node.left)
                    build_col_trees(row_tree_node.right)


                row_tree = self._build(0, self.nrows - 1, True)
                build_col_trees(row_tree)
                return row_tree


            self.row_tree = build_tree()
            for row in range(self.nrows):
                for col in range(self.ncols):
                    self.update(row, col, matrix[row][col])


        def update(self, row, col, value):
            assert 0 <= row < self.nrows and 0 <= col < self.ncols
            delta = value - self.current_values[row][col]
            self.current_values[row][col] = value
            row_node = self.row_tree
            while True:
                if row_node.index >= row:
                    # Need to update ``row_node.col_tree``
                    col_node = row_node.col_tree
                    while col_node.index != col:
                        if col_node.index > col:
                            col_node.left_and_self_weight += delta
                            col_node = col_node.left
                        else:
                            col_node = col_node.right
                    col_node.left_and_self_weight += delta
                    if row_node.index == row:
                        break
                    else:
                        row_node = row_node.left
                else:
                    row_node = row_node.right


        def sumRegion(self, row, col):
            assert row < self.nrows and col < self.ncols
            if row >= 0 and col >= 0:
                rv = 0
                row_node = self.row_tree
                while True:
                    if row_node.index <= row:
                        col_node = row_node.col_tree
                        while col_node.index != col:
                            if col_node.index < col:
                                rv += col_node.left_and_self_weight
                                col_node = col_node.right
                            else:
                                col_node = col_node.left
                        rv += col_node.left_and_self_weight
                        if row_node.index == row:
                            break
                        else:
                            row_node = row_node.right
                    else:
                        row_node = row_node.left

                return rv
            else:
                return 0



        @classmethod
        def _build(cls, index_lower, index_upper, is_row_node):
            if index_lower > index_upper:
                return None
            index_mid = (index_lower + index_upper) // 2
            node = cls.Node(index_mid, is_row_node)
            node.left = cls._build(index_lower, index_mid - 1, is_row_node)
            node.right = cls._build(index_mid + 1, index_upper, is_row_node)
            return node



    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) > 0 and len(matrix[0]) >= 0:
            self.tree = self.TwoDTree(matrix)


    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.tree.update(row, col, val)


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (self.tree.sumRegion(row2, col2) +
                self.tree.sumRegion(row1 - 1, col1 - 1) - 
                self.tree.sumRegion(row1 - 1, col2) -
                self.tree.sumRegion(row2, col1 - 1))
        
        

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)


def test1():
    matrix = [
          [3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(2,1,4,3) == 8
    assert num_matrix.sumRegion(0,0,2,2) == 21
    num_matrix.update(3,2,2)
    assert num_matrix.sumRegion(2,1,4,3) == 10


def test2():
    matrix = [
        [1]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(0,0,0,0) == 1
    num_matrix.update(0,0,3)
    assert num_matrix.sumRegion(0,0,0,0) == 3


def test3():
    matrix = [
        [1,2,3]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(0,0,0,0) == 1
    assert num_matrix.sumRegion(0,0,0,2) == 6
    num_matrix.update(0,0,3)
    num_matrix.update(0,1,3)
    num_matrix.update(0,2,3)
    assert num_matrix.sumRegion(0,0,0,0) == 3
    assert num_matrix.sumRegion(0,0,0,2) == 9
    num_matrix.update(0,2,4)
    assert num_matrix.sumRegion(0,0,0,2) == 10


def test4():
    matrix = [
        [1],[2],[3]
    ]
    num_matrix = NumMatrix(matrix)
    assert num_matrix.sumRegion(0,0,0,0) == 1
    assert num_matrix.sumRegion(0,0,2,0) == 6
    num_matrix.update(0,0,3)
    num_matrix.update(1,0,3)
    num_matrix.update(2,0,3)
    assert num_matrix.sumRegion(0,0,0,0) == 3
    assert num_matrix.sumRegion(0,0,2,0) == 9
    num_matrix.update(2,0,4)
    assert num_matrix.sumRegion(0,0,2,0) == 10


def test5():
    # A stupid test for leetcode
    num_matrix = NumMatrix([])
