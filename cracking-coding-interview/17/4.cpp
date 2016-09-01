#include <cstdio>

int get_sign(int a) {
    return 1 - ((unsigned(a)) >> 31) * 2;
}

int max_without_if_and_comparison(int a, int b) {
    int difference = a - b;
    return ((a + b) + get_sign(difference) * (difference)) / 2;
}

void print_get_sign_result(int a) {
    printf("Sign of %d: %d\n", a, get_sign(a));
}

void print_max_result(int a, int b) {
    printf("Max of %d, %d: %d\n", a, b, max_without_if_and_comparison(a, b));
}

int main(int argc, char *argv[])
{
    print_get_sign_result(0);
    print_get_sign_result(-1);
    print_get_sign_result(1);
    print_get_sign_result(11111);
    print_get_sign_result(-11111);
    
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

    // Special cases that function fails because of overflow
    print_max_result(0x7fffffff, -2);
    
    return 0;
}
