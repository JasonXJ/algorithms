#include <string>

using namespace std;

/* The idea is that we "grow" the string. For example, the string is
 * "ABCD". We will grow it from "D" to "CD" and to "BCD" and finally
 * "ABCD".
 *
 * The number corresponding to "D" is clear, which is 4.  Then we grow
 * the number to "CD". How do we generate "CD" from "D"?  Adding 26 to
 * "D" results in "AD". Adding another 26 results in "BD". So,
 * clearly, "CD" is "D" plus 3 rounds of "'A' to 'Z'", which is 4 + 26*3. 
 * 
 * Then we need to grow "CD" to "BCD". We use the similar method:
 * "BCD" is "CD" plus 2 rounds of "'AA' to 'ZZ'", which is 4 + 26*3 +
 * 26*26*2. Similarly, "ABCD" is "BCD" plus 1 round of " 'AAA' to
 * 'ZZZ' ", which is 4 + 26*3 + 26*26*2 + 26*26*26*1.
 */
class Solution {
public:
    int titleToNumber(string s) {
        int rv = 0;
        int base = 1;
        for (int i = int(s.size() - 1); i >= 0; --i) {
            rv += base * (s[i] - 'A' + 1);
            base *= 26;
        }

        return rv;
    }
};
