struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};


#include <vector>

using namespace std;

class Solution {
    vector<int> temp_rv;

    void pathSum(TreeNode* root, int sum, vector<vector<int>>& rv) {
        temp_rv.push_back(root->val);
        if (root->left == nullptr && root->right == nullptr) {
            if (sum == root->val)
                rv.push_back(temp_rv);
        }
        else {
            if (root->left != nullptr) {
                pathSum(root->left, sum - root->val, rv);
            }
            if (root->right != nullptr) {
                pathSum(root->right, sum - root->val, rv);
            }
        }
        temp_rv.pop_back();
    }

public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if (root == nullptr)
            return {};

        temp_rv.clear();
        vector<vector<int>> rv;
        pathSum(root, sum, rv);
        return rv;
    }
};
