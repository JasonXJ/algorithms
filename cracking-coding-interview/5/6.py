def swap_odd_even(x):
    # The ``x`` cannot have more than 32 bits.
    assert x >> 32 == 0
    even_mark = 0x55555555
    odd_mark = 0xaaaaaaaa

    return ((x & even_mark) << 1) | ((x & odd_mark) >> 1)

def test_swap_odd_even():
    assert swap_odd_even(0b10101010) == 0b01010101
    assert swap_odd_even(0b00000000) == 0b00000000
    assert swap_odd_even(0b11111111) == 0b11111111
    assert swap_odd_even(0b10011001) == 0b01100110
