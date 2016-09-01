# This is an O(3) solution.
class Solution(object):
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        assistant_matrix = self._getAssistantMatrix(matrix)
        ROWS = len(matrix)
        COLS = len(matrix[0])
        max_area = 0
        for start_row_index in range(ROWS):
            if (ROWS - start_row_index) * COLS < max_area:
                # No need to continue anymore
                return max_area
            for end_row_index in range(ROWS-1, start_row_index-1, -1):
                height = end_row_index - start_row_index + 1
                col_index = 0
                end_row = assistant_matrix[end_row_index]
                while True:
                    # Find the starting column
                    while col_index < COLS:
                        if end_row[col_index] >= height:
                            start_col = col_index
                            break
                        col_index += 1
                    else:  # Cannot find the start column
                        break
                    col_index += 1

                    # Find the ending column
                    while col_index < COLS:
                        if end_row[col_index] < height:
                            break
                        col_index += 1
                    area = (col_index - start_col) * height
                    if area > max_area:
                        max_area = area
                    col_index += 1

        return max_area


    @classmethod
    def _getAssistantMatrix(cls, matrix):
        row = [None] * len(matrix[0])
        # The value of assistant[i][j] means matrix[i - assistant[i][j]][j] is
        # the first 0 above matrix[i][j].
        assistant = [row[:] for _ in range(len(matrix))]

        # Init the first row
        first_row = assistant[0]
        for i_col, x in enumerate(matrix[0]):
            if x == '0':
                first_row[i_col] = 0
            else:
                first_row[i_col] = 1

        # Init other rows
        for i_row in range(1, len(matrix)):
            matrix_row = matrix[i_row]
            last_row = assistant[i_row-1]
            current_row = assistant[i_row]

            for i_col, x in enumerate(matrix_row):
                if x == '0':
                    current_row[i_col] = 0
                else:
                    current_row[i_col] = last_row[i_col] + 1

        return assistant

def test():
    f = Solution().maximalRectangle
    assert f([['0','0','0','0'], ['0','1','1','0'], ['0','1','1','0'], ['0','1','0','0']]) == 4
    assert f([['0','0','0','0'], ['0','1','1','0'], ['0','1','1','0'], ['0','1','1','0']]) == 6

def print_matrix(m, width=0):
    format_str = '{:>' + str(width) + '}'
    for row in m:
        for element in row:
            print(format_str.format(element), end='')
        print()

if __name__ == "__main__":
    data = ["1111111111111101001111111100111011111111","1111011011111111101101111101111111111111","0111101011111101101101101111111111111111","0101101011111111111101111111010110111111","1111111111110111110110010111111111111111","1111111110110101111111111101011111101111","0110110101110011111111111111110111110101","0111111111111100111111100110011011010101","1111011110111111111011011011110101101011","1111111110111111111101101101110111101111","1110110011111111111100111111111111111111","1011111110111101111001110111111111111111","0110111111111111101111110111011111011111","1111111111111111011111111111110111111011","1111100111111110101100111111111111101111","1111101111111110111111011111111111011111","1111101111111111111111011001111110011111","1111110111111111011111111111110111110111","1011111111111111010111110010111110111111","1111110011111111111110111111111111111011","1111111111111111110111011111011111011011","1100011011111111111111011111011111111111","1111101011111111111101100101110011111111","1110010111111111111011011110111101111101","1111111111111101101111111111101111111111","1111111011111101111011111111111110111111","1110011111111110111011111111110111110111","1111111111111100111111010111111111110111","1111111111111111111111000111111111011101","1111110111111111111111111101100111011011","1111011011111101101101111110111111101111","1111111111011111111111111111111111111111","1111111111111111111111111111111111111111","1100011111111110111111111111101111111011","1111101111111101111010111111111111111111","0111111111110011111111110101011011111111","1011011111101111111111101111111111110011","1010111111111111111111111111111110011111","0111101111011111111111111111110111111111","0111111011111111011101111011101111111111","0111111111110101111011111101011001111011","1111111111111011110111111101111111101110","1111101111111100111111111110111111001111","1101101111110101111101111111100111010100","0110111111100111110010111110111011011101"]
    print_matrix(data)

    # import ipdb; ipdb.set_trace()
    f = Solution().maximalRectangle
    print(f(data))

    for i in range(len(data)):
        data[i] = list(data[i])
    print(f(data))
