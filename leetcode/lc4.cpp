#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution
{
public:
    static inline int calc_medium(int start, int end) {
        return floor((start + end) / 2.);
    }

    static inline int calc_medium2(int medium, int k) {
        return k - (medium + 1) - 1;
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size())
            return findMedianSortedArrays(nums2, nums1);

        assert(nums2.size() != 0);

        // Find the k smallest numbers in the two array
        size_t k = (nums1.size() + nums2.size() + 2) / 2;

        int start = 0, end = nums1.size() - 1;
        int medium, medium2;
        medium = calc_medium(start, end);
        medium2 = calc_medium2(medium, k);

        while (start <= end) {
            if (medium >= 0 && medium2 + 1 < (int) nums2.size() && nums1[medium] > nums2[medium2+1])
                end = medium - 1;
            else if (medium2 >= 0 && medium + 1 < (int) nums1.size() && nums2[medium2] > nums1[medium+1])
                start = medium + 1;
            else
                break;

            medium = calc_medium(start, end);
            medium2 = calc_medium2(medium, k);
        }

        // Find the largest number in the k smallest numbers.
        vector<int> largest;
        assert(medium < (int) nums1.size());
        if (medium >= 0)
            largest.push_back(nums1[medium]);
        if (medium - 1 >= 0)
            largest.push_back(nums1[medium - 1]);
        if (medium2 >= 0)
            largest.push_back(nums2[medium2]);
        if (medium2 - 1 >= 0)
            largest.push_back(nums2[medium2 - 1]);
        assert(largest.size() > 0);
        sort(largest.begin(), largest.end());
        if ((nums1.size() + nums2.size()) & 0x1)  // Odd total length.
            return largest[largest.size() - 1];
        else
            return (largest[largest.size() - 1] + largest[largest.size() - 2]) / 2.;
    }
};

int main(int argc, char *argv[])
{
    (void) argc;
    (void) argv;

    Solution s;

    {
        vector<int> nums1 = {1};
        vector<int> nums2 = {};
        cout << s.findMedianSortedArrays(nums1, nums2) << endl;
    }
    {
        vector<int> nums1 = {1,2};
        vector<int> nums2 = {};
        cout << s.findMedianSortedArrays(nums1, nums2) << endl;
    }
    {
        vector<int> nums1 = {4,5};
        vector<int> nums2 = {6};
        cout << s.findMedianSortedArrays(nums1, nums2) << endl;
    }
    {
        vector<int> nums1 = {1,2};
        vector<int> nums2 = {3,4};
        cout << s.findMedianSortedArrays(nums1, nums2) << endl;
    }

    return 0;
}
