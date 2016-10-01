#include <string>
#include <cstdlib>

using namespace std;

class Solution {
    bool check(const string &num, size_t start, int num1, int num2) {
        while (start < num.size()) {
            int expect = num1 + num2;
            int expect_length = length(expect);
            if (start + expect_length > num.size())
                return false;
            if (atoi(num.substr(start, expect_length).c_str()) != expect)
                return false;
            start += expect_length;
            num1 = num2;
            num2 = expect;
        }

        return true;
    }

    int length(int val) {
        int l = 0;
        do {
            l += 1;
            val /= 10;
        } while (val != 0);
        return l;
    }
public:
    bool isAdditiveNumber(string num) {
        if (num.size() < 3)
            return false;
        size_t end1_max = num.size() - 2;
        if (num[0] == '0')
            end1_max = 1;

        int num1 = 0, num2;
        for (size_t end1 = 1; end1 <= end1_max; ++end1) {
            num1 = num1 * 10 + num[end1 - 1] - '0';
            num2 = 0;
            size_t num2_max = num.size() - 1;
            if (num[end1] == '0')
                num2_max = end1 + 1;
            for (size_t end2 = end1 + 1; end2 <= num2_max; ++end2) {
                num2 = num2 * 10 + num[end2 - 1] - '0';
                if (check(num, end2, num1, num2))
                    return true;
            }
        }

        return false;
    }
};


#include <iostream>
int main(void)
{
    cout << (Solution().isAdditiveNumber("112358") == true) << endl;
    cout << (Solution().isAdditiveNumber("199100199") == true) << endl;
    cout << (Solution().isAdditiveNumber("199100190") == false) << endl;
    cout << (Solution().isAdditiveNumber("11") == false) << endl;
    cout << (Solution().isAdditiveNumber("101") == true) << endl;
    return 0;
}
