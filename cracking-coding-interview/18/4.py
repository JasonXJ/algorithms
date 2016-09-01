def decimal_digit_count(n):
    assert n >= 0
    count = 1
    n /= 10
    while n:
        count += 1
        n /= 10

    return count

def count_2s(n):
    if n <= 0:
        return 0

    decimal_digits = decimal_digit_count(n)
    twos = 0

    divisor = 10 # 除数: divisor, 被除数: divident, 商: quotient
    multiplier = 1 # 乘数: multiplier, 被乘数: multiplicand, 乘积: product
    for i in range(decimal_digits):
        twos += n // divisor * multiplier
        twos += count_remain_2s(n, i)

        divisor *= 10
        multiplier *= 10

    return twos

def count_remain_2s(n, i):
    base = 10 ** i
    temp = n % (base * 10) - (2 * base - 1)
    if temp < 0:
        return 0
    if temp > base:
        return base
    return temp

def count_2s_naive(n):
    def count_2s_single_number(n):
        count = 0
        while n > 0:
            n, r = divmod(n, 10)
            if r == 2:
                count += 1
        return count

    count = 0
    for i in range(0, n+1):
        count += count_2s_single_number(i)

    return count

def test_count_2s():
    for i in range(100000):
        assert count_2s(i) == count_2s_naive(i)
