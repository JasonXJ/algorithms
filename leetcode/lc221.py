from collections import namedtuple

Info = namedtuple('Info', 'left, up, max_size')

# O(n*m) solution
class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        data_matrix = [[None] * ncols for i in range(nrows)]

        # Init first row
        input_first_row = matrix[0]
        first_row = data_matrix[0]
        for i in range(ncols):
            # Note that for first row we don't care about ``Info.left``
            value = int(input_first_row[i])
            first_row[i] = Info(None, value, value)

        # Init first column
        for row_no in range(1, nrows):
            # Note that for first column we don't care about ``Info.up``
            value = int(matrix[row_no][0])
            data_matrix[row_no][0] = Info(value, None, value)

        # Calculate others entries
        for row_no in range(1, nrows):
            input_row = matrix[row_no]
            row = data_matrix[row_no]
            last_row = data_matrix[row_no - 1]
            for col_no in range(1, ncols):
                if input_row[col_no] == '0':
                    row[col_no] = Info(0, 0, 0)
                else:
                    left = row[col_no - 1].left + 1
                    up = last_row[col_no].up + 1
                    max_size = min(left, up, last_row[col_no - 1].max_size + 1)
                    row[col_no] = Info(left, up, max_size)

        # Return the largest `max_size`.
        return max(x.max_size for row in data_matrix for x in row)**2


# This is a O(n*m) complicated solution using Stack
class StackSolution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        int_matrix = [[int(x) for x in row] for row in matrix]

        last_row = int_matrix[0]
        for row in int_matrix[1:]:
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] += last_row[i]
            last_row = row

        max_square = 0
        for row, max_height in zip(reversed(int_matrix), range(len(int_matrix), 0, -1)):
            if max_square > max_height:
                break
            current_square = self.rowMax(row)
            print('{}: {}'.format(row, current_square))
            if current_square > max_square:
                max_square = current_square

        return max_square**2


    def analyzeStack(self, stack, start=0):
        total_width = remain_width = sum(x[1] for x in stack[start:])
        max_square = 0
        for height, width in stack[start:]:
            current_square = min(height, remain_width)
            if current_square > max_square:
                max_square = current_square
            remain_width -= width

        return total_width, max_square

    
    def rowMax(self, row):
        # Each element of `stack` is ``[height, width]``.  `stack` is always in
        # strictly increasing order with regard to the height.
        stack = []  
        max_square = 0
        for x in row:
            last_height = -1
            if len(stack) > 0:
                last_height = stack[-1][0]
            if last_height < x:  # Order already preserved
                stack.append([x, 1])
            else:  # Shrink and merge
                last_higher = len(stack) - 1
                while last_higher >= 0 and stack[last_higher][0] >= x:
                    last_higher -= 1
                last_higher += 1
                total_width, current_square = self.analyzeStack(stack, last_higher)
                if current_square > max_square:
                    max_square = current_square
                del stack[last_higher:]
                stack.append([x, total_width+1])

        _, current_square = self.analyzeStack(stack)
        return max(max_square, current_square)


def test(colapsed_matrix):
    print('Matrix:')
    for s in colapsed_matrix:
        print(s)
    matrix = [list(s) for s in colapsed_matrix]
    rv = Solution().maximalSquare(matrix)
    print('Result: ', rv)
    return rv


if __name__ == "__main__":
    test(["1010","1011","1011","1111"])
    test(["0010","1111","1111","1110","1100","1111","1110"])
