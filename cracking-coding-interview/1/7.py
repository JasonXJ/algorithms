def expand_zero(matrix):
    M = len(matrix)
    if M == 0:
        return matrix
    N = len(matrix[0])

    row_to_zero = set()
    col_to_zero = set()
    for row in range(M):
        for col in range(N):
            if matrix[row][col] == 0:
                row_to_zero.add(row)
                col_to_zero.add(col)

    for row in row_to_zero:
        for col in range(N):
            matrix[row][col] = 0

    for col in col_to_zero:
        for row in range(M):
            matrix[row][col] = 0

    return matrix

if __name__ == '__main__':
    assert (expand_zero([]) == [])
    assert (
        expand_zero(
            [[1,1,1],
             [1,0,1],
             [1,1,1]]) ==
        [[1,0,1],
         [0,0,0],
         [1,0,1]]
    )
    print('tests passed...')
