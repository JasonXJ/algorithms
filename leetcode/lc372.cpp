#include <vector>

using namespace std;

class Solution {
public:
    int superPow(int a, vector<int>& b) {
        const int MOD_NUMBER = 1337;
        int base = a % MOD_NUMBER;
        int current_value = 1;

        for (size_t cursor = b.size(); cursor != 0; --cursor) {
            int new_value = 1;
            for (int i = 0, i_end = b[cursor-1]; i < i_end; ++i) {
                new_value *= base;
                new_value %= MOD_NUMBER;
            }
            current_value *= new_value;
            current_value %= MOD_NUMBER;

            int old_base = base;
            for (int i = 0; i < 9; ++i) {
                base *= old_base;
                base %= MOD_NUMBER;
            }
        }

        return current_value;
    }
};

#include <iostream>

int main(void)
{
    vector<int> b = {1, 0};
    cout << Solution().superPow(2, b) << endl;
    return 0;
}
