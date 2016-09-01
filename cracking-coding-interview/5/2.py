def float_to_binary(f):
    BINARY_LENGTH = 32

    assert 0 <= f <= 1
    binary = ['0' for i in range(32)]
    base = 1.
    for i in range(BINARY_LENGTH):
        if f == 0:
            break
        base /= 2
        if f >= base:
            f -= base
            binary[i] = '1'

    if f != 0:
        return None
    else:
        return ''.join(binary)

def binary_to_float(*bit_positions):
    f = 0
    for x in bit_positions:
        f += 2**-x

    return f

def test_1():
    assert float_to_binary(0.72) is None
    assert binary_to_float(1, 3, 7) == 0.6328125
    assert float_to_binary(binary_to_float(1, 3, 7)) == '10100010000000000000000000000000'
