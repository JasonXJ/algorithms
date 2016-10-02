#include <vector>
#include <cassert>

using namespace std;

/* O(n) time, O(1) space. Credit:
 * https://discuss.leetcode.com/topic/21605/accepted-c-java-o-n-time-o-1-space-easy-solution-with-detail-explanations */
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xor_of_the_two = 0;
        for (auto &x: nums)
            xor_of_the_two ^= x;
        assert(xor_of_the_two != 0);

        /* mask is a binary number with only the right most "1" bit of
         * `xor_of_the_two` set. For example, if xor_of_the_two ==
         * 1010, then mask == 0010 */
        int mask = xor_of_the_two & - xor_of_the_two;

        int xor1 = 0, xor2 = 0;
        for (auto &x: nums) {
            if (x & mask)
                xor1 ^= x;
            else
                xor2 ^= x;
        }

        return {xor1, xor2};
    }
};
