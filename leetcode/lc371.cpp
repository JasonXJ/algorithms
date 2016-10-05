class Solution {
public:
    int getSum(int a, int b) {
        int rv = 0;
        unsigned mask = 1;
        int carry = 0;
        while (mask != 0) {
            int ax = a & mask;
            int bx = b & mask;
            if (ax != 0 && bx != 0 && carry != 0)
            {
                rv |= mask;
            }
            else if ((ax != 0 && bx == 0 && carry == 0) ||
                    (ax == 0 && bx != 0 && carry == 0) || 
                    (ax == 0 && bx == 0 && carry != 0))
            {
                rv |= mask;
                carry = 0;
            }
            else if (!(ax == 0 && bx == 0 && carry == 0)) {
                carry = 1;
            }
            mask <<= 1;
        }
        return rv;
    }
};


#include <iostream>
using namespace std;
int main(void)
{
    cout << Solution().getSum(77, 33) << endl;
    cout << Solution().getSum(50, 20) << endl;
    cout << Solution().getSum(-50, 20) << endl;
    return 0;
}
