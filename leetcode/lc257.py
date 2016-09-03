# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        rv = []
        prefix = []
        def dfs(node):
            if node is None:
                return
            prefix.append(str(node.val))
            if node.left is None and node.right is None:
                rv.append('->'.join(prefix))
            else:
                dfs(node.left)
                dfs(node.right)
            prefix.pop()


        dfs(root)

        return rv;
