#include <vector>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> rv;
        int left = 0, right = numbers.size() - 1;
        while (left < right) {
            int temp = numbers[left] + numbers[right];
            if (temp == target) {
                rv.push_back(left+1);
                rv.push_back(right+1);
                break;
            } else if (temp < target) {
                ++left;
            } else {
                --right;
            }
        }

        return rv;
    }
};
