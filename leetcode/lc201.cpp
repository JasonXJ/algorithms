#include <cassert>

class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        assert(m <= n);

        int moved = 0;

        while(m != n) {
            m >>= 1;
            n >>= 1;
            ++moved;
        }

        return m << moved;
    }
};

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    (void) argc;
    (void) argv;

    cout << Solution().rangeBitwiseAnd(2, 3) << endl;

    return 0;
}
