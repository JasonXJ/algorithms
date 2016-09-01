#include <iostream>
#include <cstring>

using std::cout;
using std::endl;

void ReplaceSpace(char *str, int true_length) {
    const char *replace_to = "%20";
    const int length_of_replace_to = 3;

    int num_spaces = 0;

    for (int i = 0; i < true_length; ++i)
        if (str[i] == ' ')
            ++num_spaces;
    // Let `p_source` point to the end of the string.
    char *p_source = &str[true_length-1];
    char *p_target = p_source + num_spaces * (length_of_replace_to - 1);

    while (num_spaces != 0) {
        if (*p_source == ' ') {
            --num_spaces;
            p_target -= length_of_replace_to;
            --p_source;
            char *p_temp = p_target;
            for (int i = 0; i < length_of_replace_to; ++i)
                *(++p_temp) = replace_to[i];
        } else {
            *(p_target--) = *(p_source--);
        }
    }
}

int main(int argc, char *argv[]) {
    char a[] = "", b[] = "hello", c[] = "hello world  ", d[] = " hello world       ";
    int length_a = 0, length_b = 5, length_c = 11, length_d = 13;
    ReplaceSpace(a, length_a);
    ReplaceSpace(b, length_b);
    ReplaceSpace(c, length_c);
    ReplaceSpace(d, length_d);

    cout << a << endl
        << b << endl
        << c << endl
        << d << endl;
}
