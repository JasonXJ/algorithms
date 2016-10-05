#include <string>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string reversed_rv;
        bool carry = 0;
        size_t ai = a.size();
        size_t bi = b.size();
        while (ai > 0 || bi > 0 || carry != 0) {
            int ax = 0, bx = 0;
            if (ai > 0) {
                --ai;
                ax = a[ai] - '0';
            }
            if (bi > 0) {
                --bi;
                bx = b[bi] - '0';
            }
            int result = ax + bx + carry;
            if (result >= 2) {
                carry = 1;
                result -= 2;
            } else {
                carry = 0;
            }
            if (result != 0)
                reversed_rv.push_back('1');
            else
                reversed_rv.push_back('0');
        }

        return string(reversed_rv.rbegin(), reversed_rv.rend());
    }
};
