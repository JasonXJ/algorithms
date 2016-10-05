#include <vector>
#include <cstdio>
#include <iostream>
#include <cassert>
#include <random>
#include <ctime>

using namespace std;


/* O(n) time and O(1) space solution (note that unlike
 * PartitionSolution, this one does not modify the input array and
 * the worst case complexity (instead of the average complexity) is
 * O(n))
 *
 *
 * References:
 *
 * 1. https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
 * 2. https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration
 *
 *
 * Proof:
 *
 * Since we scan the array again at the end to count the actual
 * appearances of `candidate1` and `candidate2`, what we need to prove
 * is that if a value is one of the majority values, it must equal
 * either `candidate1` or `candidate2` at the end of the first for
 * loop.
 *
 * Let's take a look at the "else" clause of the first for loop. We
 * can consider this step generating a triplet {x, y, z}, where x is
 * the current element of the array that we are processing, y is one
 * of the element with value candidate1 and z is one of the element
 * with value candidate2. Note that we can prove that the values of x,
 * y and z must be different from each other. When the first for loop
 * is completed, it is obvious that every element of the input array
 * is in exactly one of the triplet, except for count1 of the elements
 * with value candidate1 and count2 of the elements with candidate2.
 * These count1 + count2 elements are not in any triplets.
 *
 * Let's assume that m is a majority value and m equals neither
 * candidate1 nor candidate2 when the loop is completed. Let's say
 * value m appears k times in the input array. Thus, k > floor(n/3) by
 * definition, where n is the size of the input array.  Since the
 * three elements of a triplet must have different values, there must
 * be exactly k triplets generated in the above-mentioned "else"
 * clause which contain an element with value m. Obviously, these m
 * triplets contain totally 3k > n different elements, which
 * contradicts the fact that the input array has only n elements.
 * Therefore, m must equal candidate1 or candidate2 when the loop is
 * completed.
 *
 * */
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int candidate1 = 0, count1 = 0;
        int candidate2 = 1, count2 = 0;
        // First scan.
        for (const auto &x : nums) {
            if (candidate1 == x)
                ++count1;
            else if (candidate2 == x)
                ++count2;
            else if (count1 == 0)
            {
                candidate1 = x;
                count1 = 1;
            }
            else if (count2 == 0)
            {
                candidate2 = x;
                count2 = 1;
            }
            else
            {
                // Generate a "triplet".
                --count1;
                --count2;
            }
        }

        vector<int> rv;
        count1 = 0;
        count2 = 0;
        // Second scan.
        for (const auto &x : nums) {
            if (x == candidate1)
                ++count1;
            else if (x == candidate2)
                ++count2;
        }

        if (count1 > int(nums.size() / 3))
            rv.push_back(candidate1);
        if (count2 > int(nums.size() / 3))
            rv.push_back(candidate2);
        return rv;
    }
};


/* O(n) average time and O(1) *extra* (this solution will modify the
 * input vector) space solution using partition. Note that there is a
 * post about using some majority vote algorithm which does not
 * modify the array:
 * https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration
 * */
class PartitionSolution {
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
