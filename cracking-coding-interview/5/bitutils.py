def test_bit(x, i):
    return (x & (0x1 << i)) != 0

def set_bit(x, i):
    return x | (0x1 << i)

def reset_bit(x, i):
    return x & ~(0x1 << i)

def highest_1_bit_pos(x):
    if x == 0:
        return -1
    x >>= 1
    highest_bit = 0
    while x != 0:
        x >>= 1
        highest_bit += 1
    return highest_bit
