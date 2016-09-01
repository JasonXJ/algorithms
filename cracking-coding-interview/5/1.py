def insert(N, M, i, j):
    # XXX: This is actually not an "insert". It is a "replace".

    # Clear `i` to `j` bits in `N`
    N &= ~(((0b1 << (j-i+1)) - 1) << i)

    # "Insert" M
    N |= M << i

    return N

def test_1():
    assert insert(0b10000, 0b101, 1, 3) == 0b11010
    assert insert(0b10001, 0b101, 1, 3) == 0b11011
    assert insert(0b11111, 0b000, 1, 3) == 0b10001
