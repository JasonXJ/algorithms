from bitutils import test_bit as tb, set_bit, reset_bit

def next_(x):
    """ Find the smallest number larger than `x` and has the same number of 1 bits as `x` 

    Idea: For a positive number `x`, we always can find the suffix `s` of the
    style "0b011...100...0", where the number of "0" in the tail >= 0, and the
    number of "1"s > 0. For the next number, we only need to modify the suffix
    (we can continuously add 1 to `x` and before changes are made to the
    non-suffix part, we can always find a number satisfing the requirement).
    First, we need to make the suffix larger, the only way to do this while
    keeping the same number of 1 bits is setting the highest bit of the suffix
    to 1, i.e., the suffix will like "0b1....". Finally, we want the suffix be
    the smallest one, so the suffix should like "0b100...0111...1".

    """

    assert x > 0

    first_1_bit = 0
    while not tb(x, first_1_bit):
        first_1_bit += 1

    afterward_first_0_bit = first_1_bit + 1
    while tb(x, afterward_first_0_bit):
        afterward_first_0_bit += 1

    the_1_bit_count = afterward_first_0_bit - first_1_bit

    # Change the suffix
    x = set_bit(x, afterward_first_0_bit)
    clear_mark = ~((0b1 << afterward_first_0_bit) - 1)
    # Remember to reduce 1 from `the_1_bit_count` (because the highest bit of
    # the suffix is set to 1)
    setting_mark = (0b1 << (the_1_bit_count-1)) - 1
    x &= clear_mark
    x |= setting_mark

    return x

def prev(x):
    """ Find the largest number smaller than ... (see ``next()``) """

    assert x > 0

    # The algorithm is similar to ``next()``. The "suffix" should be "0b100..011..1"

    first_0_bit = 0
    while tb(x, first_0_bit):
        first_0_bit += 1

    afterward_first_1_bit = first_0_bit + 1
    while not tb(x, afterward_first_1_bit):
        afterward_first_1_bit += 1

    the_1_bit_count = first_0_bit + 1
    the_0_bit_count = afterward_first_1_bit - first_0_bit

    # Change the suffix

    x = reset_bit(x, afterward_first_1_bit)
    # Clear the suffix except the highest bit
    x = x >> afterward_first_1_bit << afterward_first_1_bit
    # Set the 1 bits
    x |= ((0x1 << the_1_bit_count) - 1) << (the_0_bit_count - 1)

    return x

def test_1():
    assert next_(0b110011) == 0b110101
    assert next_(0b11001) == 0b11010
    assert next_(0b1101100) == 0b1110001
    assert next_(0b110100) == 0b111000
    assert prev(0b110101) == 0b110011
    assert prev(0b11010) == 0b11001
    assert prev(0b1110001) == 0b1101100
    assert prev(0b111000) == 0b110100
