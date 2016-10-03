#include <vector>
#include <cstdio>
#include <iostream>
#include <cassert>
#include <random>
#include <ctime>

using namespace std;


/* O(n) time and O(1) *extra* (this solution will modify the input
 * vector) space solution using partition. Note that there is a post
 * about using some majority vote algorithm which does not modify the
 * array:
 * https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration
 * */
class Solution {
    void partition(vector<int>::iterator start,
            vector<int>::iterator end, int offset) {

        while (true) {
            assert(start + offset < end);
            int temp = rand() % (end - start);
            swap(*(start + temp), *(end - 1));

            auto i = start;
            auto j = start;
            auto k = start;
            int x = *(end - 1);
            while (k < end - 1) {
                int val = *k;
                if (val <= x) {
                    swap(*k, *j);
                    if (val < x) {
                        swap(*j, *i);
                        ++i;
                    }
                    ++j;
                }
                ++k;
            }
            swap(*j, *k);
            ++j;
            ++k;
            int x_offset_start = i - start;
            int x_offset_end = j - start;
            if (x_offset_start <= offset && offset < x_offset_end)
                return;
            if (x_offset_start > offset) {
                end = i;
            } else {
                // offset >= x_offset_end
                offset -= j - start;
                start = j;
            }
        }
    }

    int count_side(const vector<int>& nums, int index, int direction)
    {
        int x = nums[index];
        int count = 0;
        index += direction;
        while (index >= 0 && index < int(nums.size()) && nums[index] == x) {
            ++count;
            index += direction;
        }
        return count;
    }


public:
    vector<int> majorityElement(vector<int>& nums) {
        srand(time(0));

        int times = nums.size() / 3 + 1;
        int left, right;
        auto start = nums.begin();
        vector<int> rv;
        while (start + times <= nums.end()) {
            partition(start, nums.end(), times - 1);
            int index = (start + times - 1) - nums.begin();
            left = count_side(nums, index, -1);
            right = count_side(nums, index, 1);
            if (left + right + 1 >= times) {
                rv.push_back(nums[index]);
            }
            start = start + times + right;
        }

        return rv;
    }
};



ostream &operator<<(ostream &out, const vector<int> x) {
    out << '[';
    for (auto &e:x) {
        out << e << ',';
    }
    out << ']';
    return out;
}


int main(void)
{
    vector<int> nums[] = {
        {},
        {0},
        {0,0},
        {0,1,5,5,6,7},
        {0,1,5,5,5,7},
        {1,2,2,3,3,4,4,5,1,1,1,1},
    };
    for (auto &n:nums) {
        cout << Solution().majorityElement(n) << endl;;
    }
    
    return 0;
}
