#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int findDuplicate(const vector<int>& nums) {
        int l = 1, r = nums.size() - 1, mid;

        while (l < r) {
            mid = (l + r) / 2;

            int less_count = 0;
            int equal_count = 0;
            for (size_t i = 0; i < nums.size(); ++i) {
                int current_num = nums[i];
                if (current_num == mid) {
                    if (++equal_count > 1)
                        break;
                } else if (current_num < mid) {
                    less_count += 1;
                }
            }

            if (equal_count > 1)
                break;
            if (less_count > mid - 1)
                r = mid - 1;
            else
                l = mid + 1;
        }

        return (l + r) / 2;
    }
};

int main(void)
{
    cout << Solution().findDuplicate({1, 2, 3, 4, 4, 4, 6}) << endl;
    
    return 0;
}
