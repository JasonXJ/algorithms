struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

#include <vector>

using namespace std;

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBST(nums, 0, nums.size());
    }

    TreeNode* sortedArrayToBST(const vector<int> &nums, size_t start, size_t end) {
        if (start >= end)
            return nullptr;

        size_t mi = (start + end) / 2;
        TreeNode *node = new TreeNode(nums[mi]);
        node->left = sortedArrayToBST(nums, start, mi);
        node->right = sortedArrayToBST(nums, mi + 1, end);

        return node;
    }
};
