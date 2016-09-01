import math

def _iterate_first_quartor(N):
    y = x = 0
    # The quartor should include the right boarder
    for y in range(0, (N+1)//2):
        # The quartor does not include the bottom boarder
        for x in range(0, N//2):
            yield (y, x)

def _rotate_coordinate(y, x, N):
    new_y = x
    new_x = N - 1 - y
    return new_y, new_x

def rotate(matrix):
    N = len(matrix)
    for row in matrix:
        if len(row) != N:
            raise ValueError

    for (y, x) in _iterate_first_quartor(N):
        last_quartor_value = matrix[y][x]
        # Need to rotate 4 times (one for each quartor)
        for i in range(4):
            y, x = _rotate_coordinate(y, x, N)
            # Swap values.
            matrix[y][x], last_quartor_value = last_quartor_value, matrix[y][x]

    return matrix


if __name__ == '__main__':
    assert rotate([]) == []
    assert rotate([[1]]) == [[1]]
    assert (
        rotate([[1, 2],
                [3, 4]]) ==
        [[3, 1],
         [4, 2]]
    )
    assert (
        rotate([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]) ==
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
    )
    print('test passed...')
