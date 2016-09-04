# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        rv = []
        def dfs(node, level_from_root):
            if node is None:
                return
            if level_from_root == len(rv):
                rv.append([])
            rv[level_from_root].append(node.val)
            dfs(node.left, level_from_root + 1)
            dfs(node.right, level_from_root + 1)


        dfs(root, 0)
        return list(reversed(rv))
