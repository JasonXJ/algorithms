#include <stdio.h>
#include <limits.h>

int divide(int dividend, int divisor) {
    if (divisor == 0 || (dividend == INT_MIN && divisor == -1))
        return INT_MAX;

    int negative = (dividend < 0) ^ (divisor < 0);
    int result = 0;
    int abs_divisor, abs_dividend;

    if (divisor == INT_MIN) {
        if (dividend != INT_MIN)
            return 0; // C round to 0, so it must be 0
        else
            return 1;
    }

    // Now it is safe to abs(divisor)
    if (divisor < 0)
        abs_divisor = -divisor;
    else
        abs_divisor = divisor;

    if (dividend == INT_MIN) {
        // By removing "one abs_divisor" to make abs_dividend larger
        // than INT_MIN. (We have handled the special case that
        // divisor equal -1 or 0); Note that ``INT_MIN < dividend +
        // abs_divisor < 0``.
        abs_dividend = - (dividend + abs_divisor);
        result += 1;
    } else if (dividend < 0) {
        abs_dividend = -dividend;
    } else {
        abs_dividend = dividend;
    }


    // Subtract one divisor is too slow. We subtract 2^i divisors one time.
    int temp_subtrahend, subtrahend, addend;
    while (abs_dividend >= abs_divisor) {
        subtrahend = abs_divisor;
        addend = 1;
        temp_subtrahend = subtrahend << 1;
        // Test of `temp_subtrahend > 0` is to prevent it overflows.
        while (temp_subtrahend > 0 && abs_dividend >= temp_subtrahend) {
            subtrahend = temp_subtrahend;
            addend <<= 1;
            temp_subtrahend <<= 1;
        }

        abs_dividend -= subtrahend;
        result += addend;
    }

    if (negative)
        return -result;
    return result;
}


int main(int argc, char *argv[])
{
    printf("%d\n", divide(5, 2));
    return 0;
}
