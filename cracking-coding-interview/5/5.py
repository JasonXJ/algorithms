def naive_bit_count(x):
    count = 0
    while x != 0:
        if x & 0x1:
            count += 1
        x >>= 1

    return count

_BIT_COUNT_TABLE__BIT_WIDTH = 8;
_BIT_COUNT_TABLE__MARK = (1 << _BIT_COUNT_TABLE__BIT_WIDTH) - 1
_BIT_COUNT_TABLE = [naive_bit_count(x) for x in range(1 << _BIT_COUNT_TABLE__BIT_WIDTH)]

def bit_count(x):
    """ This is a software implementation of counting the bit using precomputed table. A better way is using the dedicated hardware operator. """
    count = 0
    while x != 0:
        print(bin(x))
        count += _BIT_COUNT_TABLE[_BIT_COUNT_TABLE__MARK & x]
        x >>= _BIT_COUNT_TABLE__BIT_WIDTH

    return count

def bit_difference(a, b):
    return bit_count(a ^ b)

def test_bit_count():
    assert bit_count(0xffffffff) == 32
    assert bit_count(0xaaaaaaaa) == 16
    assert bit_count(0x55555555) == 16
    assert bit_count(0x10000000) == 1
    assert bit_count(0xa0000000) == 2

def test_bit_difference():
    assert bit_difference(31, 14) == 2
    assert bit_difference(0x1100, 0x0011) == 4
    assert bit_difference(0xaaaaaaaa, 0x55555555) == 32
    assert bit_difference(0xffff, 0xffff) == 0
