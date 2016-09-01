#include <cassert>
#include <cstddef>
#include <vector>
#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void print_tree(TreeNode *root, bool top_level=true) {
    cout << root->val;
    if (root->left != NULL) {
        cout << " (L ";
        print_tree(root->left, false);
        cout << " L)";
    }
    if (root->right != NULL) {
        cout << " (R ";
        print_tree(root->right, false);
        cout << " R)";
    }
    if (top_level)
        cout << endl;
}

class Solution {
public:
    vector<TreeNode *> generateTrees(int n) {
        if (n > 0)
            return generateSubtrees(1, n);
        else {
            vector<TreeNode *> temp;
            return temp;
        }
    }

    vector<TreeNode *> generateSubtrees(int start, int end) {
        vector<TreeNode *> result;

        if (start > end) {
            result.push_back(NULL);
        } else {
            for (int i = start; i <= end; ++i) {
                vector<TreeNode *> left_subtrees = generateSubtrees(start, i - 1);
                vector<TreeNode *> right_subtrees = generateSubtrees(i + 1, end);
                // Note that the same node might be used in multiple tree, which might be a problem especially when we need to free the space manually.
                for (int j = 0; j < left_subtrees.size(); ++j) {
                    for (int k = 0; k < right_subtrees.size(); ++k) {
                        TreeNode *new_root = new TreeNode(i);
                        new_root->left = left_subtrees[j];
                        new_root->right = right_subtrees[k];
                        result.push_back(new_root);
                    }
                }
            }
        }

        return result;
    }
};

int main(int argc, char *argv[])
{
    Solution solution;
    //vector<TreeNode *> v3 = solution.generateTrees(2);
    //vector<TreeNode *> v2 = solution.generateTrees(2);
    vector<TreeNode *> v = solution.generateTrees(3);
    for (int i = 0; i < v.size(); ++i) {
        print_tree(v[i]);
    }
    
    return 0;
}
