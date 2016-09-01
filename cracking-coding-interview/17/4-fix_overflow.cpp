#include <cstdio>

struct SubtractionSituation {
    /* Only one of the following value should equal to 1, and others
     * should equal to 0. */
    int negative_positive, positive_negative, same_sign;
};

void get_subtraction_situation(int a, int b, SubtractionSituation &ss) {
    ss.negative_positive = ss.positive_negative = ss.same_sign = 0;
    int a_is_negative = (unsigned (a)) >> 31;
    int b_is_negative = (unsigned (b)) >> 31;
    ss.negative_positive += a_is_negative && !b_is_negative;
    ss.positive_negative += !a_is_negative && b_is_negative;
    ss.same_sign += (a_is_negative && b_is_negative) || (!a_is_negative && !b_is_negative);
}

int is_negative(int a) {
    return (unsigned(a)) >> 31;
}

int is_difference_negative(int a, int b) {
    SubtractionSituation ss;
    get_subtraction_situation(a, b, ss);

    /* Use this complex expression to avoid the situation when (a-b)
     * overflow */
    return ss.negative_positive + is_negative(a - b) * ss.same_sign;
}

int max(int a, int b) {
    int b_is_larger = is_difference_negative(a, b);
    return b_is_larger * b + (1 - b_is_larger) * a;
}

void print_max_result(int a, int b) {
    printf("Max of %d, %d: %d\n", a, b, max(a, b));
}

int main(int argc, char *argv[])
{
    print_max_result(3, 3);
    print_max_result(0, 0);
    print_max_result(3, 0);
    print_max_result(0, 3);
    print_max_result(1, 3);
    print_max_result(3, 1);
    print_max_result(3, -1);
    print_max_result(-1, 3);
    print_max_result(-1, 0);
    print_max_result(0, -1);
    print_max_result(-3, -1);
    print_max_result(-1, -3);

    // Special cases that subtraction overflow
    print_max_result(0x7fffffff, -2);
    print_max_result(-2, 0x7fffffff);
    print_max_result(0, 0x80000000);
    print_max_result(0x80000000, 0);
    print_max_result(0xfff00000, 0x80000000);
    print_max_result(0x80000000, 0xfff00000);
    print_max_result(0x80000000, 0x7fffffff);
    print_max_result(0x7fffffff, 0x80000000);
    
    return 0;
}
