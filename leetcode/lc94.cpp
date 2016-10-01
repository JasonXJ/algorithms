struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};


#include <vector>

using namespace std;


struct StackElement {
    TreeNode *node;
    bool left_visited;

    StackElement(TreeNode *node) {
        this->node = node;
        left_visited = false;
    }
};
 
// Iterative solution.
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> rv;
        if (root == nullptr)
            return rv;
        vector<StackElement> stack;
        stack.push_back({root});
        while (stack.size() > 0) {
            auto &top = stack.back();
            if (!top.left_visited and top.node->left != nullptr) {
                top.left_visited = true;
                stack.push_back({top.node->left});
            } else {
                stack.pop_back();
                rv.push_back(top.node->val);
                if (top.node->right != nullptr)
                    stack.push_back({top.node->right});
            }
        }

        return rv;
    }
};
