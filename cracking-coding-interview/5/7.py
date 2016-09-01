from bitutils import highest_1_bit_pos, test_bit as tb

def find_missing_number(array):
    """ Find a missing number in array, the array is suppose to contain all
    number from 0 to `n` except for one number which is missing. So the length
    of the array implies `n` (i.e. ``n = len(array)``).

    The basic idea is that we can know that how many of the `x`th bits of all
    the `n` number should be 1. So if we add all `x`th bits, then based on if
    the sum is odd or even, we know the `x`th bit of the missing number.
    """

    n = len(array)
    if n == 0:
        return 0
    highest_bit = highest_1_bit_pos(n)

    missing_number = 0
    for bit_pos in range(highest_bit, -1, -1):
        # If we sort the ``n+1`` number, the `bit_pos`th bits of all the number
        # is periodic like 00..01...10...01..1... . And the period is
        # ``2<<bit_pos`` (i.e. ``2**(bit_pos+1)``)
        period = 2 << bit_pos

        # Inside each period, the number of 1 bits is a half of the period length
        period_count = (n+1) // period
        one_bits__periods = period_count*(period//2)

        # There are may still some 1 bits that are not contained in a completed
        # period
        one_bits__outside_periods = ((n+1) % period) - period // 2
        if one_bits__outside_periods < 0:
            one_bits__outside_periods = 0

        one_bits = one_bits__periods + one_bits__outside_periods

        one_bits_found = sum(1 for x in array if tb(x, bit_pos))
        #print('Current bit_pos={}\n\tone_bits: {} + {} = {}\n\tone_bits_found: {}\n'.format(
            #bit_pos, one_bits__periods, one_bits__outside_periods, one_bits, one_bits_found
        #))
        missing_number <<= 1
        # The bit is 1
        if one_bits_found != one_bits:
            assert one_bits_found == one_bits - 1
            missing_number += 1

    return missing_number


# The solutions in the book provide two better methods, which is implemented as
# ``find_missing_number__fast`` and ``find_missing_number__short``.

def find_missing_number__short(array):
    """ The complexity of this function is the same as
    :func:`find_missing_number`, but the code is much shorter """
    n = len(array)
    
    # We sum up all the numbers, note that we can only access one bit of a
    # number at a time, so the process of sum take O(n logn) time. However,
    # here we gonna write code that sum them directly.
    sum_array = sum(array)

    sum_should_be = n*(n+1)/2

    return sum_should_be - sum_array

def find_missing_number__fast(array):
    """ The idea of this version is that each time we figure out what the least
    significant bit of the missing number is, and then we construct a new array
    whose size is a half of the previous one. We iterate this steps until we
    find out all the bits. This algorithm has a time complexity of O(n). For
    :func:`find_missing_number` and :func:`find_missing_number__short`, if we
    consider the bits of each number we need to process to be O(log n), the
    overall complexity is O(n log n).  """

    original_n = len(array)
    if original_n == 0:
        return 0
    # `highest_bit` is the number of iteration we need.
    highest_bit = highest_1_bit_pos(original_n)
    # `missing_bits` store less significant bits at the front (i.e.
    # ``missing_bits[0]`` is the least significant bit)
    missing_bits = []

    current_array = array
    # Remember to plus 1 because the bit position starts from 1
    for i in range(highest_bit+1):
        count_0 = 0
        count_1 = 0
        for x in current_array:
            # Test the least significant bits
            if 0x1 & x:
                count_1 += 1
            else:
                count_0 += 1

        # No matter what the parity of `len(current_array)` is, if ``count_0 <=
        # count_1``, the least significant bit is 0. Otherwise it is 1. We also
        # construct a new `current_array`. For example, if we know the least
        # significant bit is 0, then we remove all the number in
        # `current_array` that have a least significant bit of 1. We also shift
        # right every number left by 1 bit. After that, `current_array` become
        # an array containing all number from 0 to ``len(current_array)``,
        # except one missing number. The next loop will figure out the next
        # least significant bit.
        if count_0 <= count_1:
            missing_bits.append(0)
            current_array = [x>>1 for x in current_array if 0x1 & x == 0]
        else:
            missing_bits.append(1)
            current_array = [x>>1 for x in current_array if 0x1 & x == 1]
    
    missing_number = 0
    for bit in reversed(missing_bits):
        missing_number <<= 1
        missing_number |= bit
    return missing_number

def test_bitutils_higest_1_bit_pos():
    assert highest_1_bit_pos(0b11011) == 4
    assert highest_1_bit_pos(0b10000) == 4
    assert highest_1_bit_pos(0b0001) == 0

def test_find_missing_number():
    def build_testing_array(n, missing):
        missing = int(missing)
        return list(range(0, missing)) + list(range(missing+1, n+1))

    for func in (find_missing_number, find_missing_number__short, find_missing_number__fast):
        for n in range(1, 101):
            for missing_number in range(n+1):
                assert func(build_testing_array(n, missing_number)) == missing_number
