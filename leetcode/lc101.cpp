struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};


// Recursive solution
class Solution {
    bool isSymmetric(TreeNode* left, TreeNode* right) {
        if (left == nullptr || right == nullptr) {
            return left == right;
        }
        if (left->val != right->val)
            return false;
        return isSymmetric(left->left, right->right) && isSymmetric(left->right, right->left);
    }

public:
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr)
            return true;
        return isSymmetric(root->left, root->right);
    }
};


#include <vector>

using namespace std;

// Iterative level-order solution
class IterativeSolution {
public:
    bool isSymmetric(TreeNode* root) {
        vector<TreeNode *> current_nodes, next_nodes;
        current_nodes.push_back(root);
        while (!current_nodes.empty()) {
            auto l = current_nodes.begin(),
                 r = current_nodes.end() - 1;
            while (l < r) {
                if (*l == nullptr || *r == nullptr)
                {
                    if (*l != *r)
                        return false;
                }
                else if ((*l)->val != (*r)->val)
                    return false;
                ++l;
                --r;
            }
            for (auto &n : current_nodes) {
                if (n != nullptr) {
                    next_nodes.push_back(n->left);
                    next_nodes.push_back(n->right);
                }
            }
            current_nodes.clear();
            next_nodes.swap(current_nodes);
        }

        return true;
    }
};
