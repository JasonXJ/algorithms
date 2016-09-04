# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current = root
        larger, smaller = p.val, q.val
        if larger < smaller:
            larger, smaller = smaller, larger
        while True:
            if current.val > larger:
                current = current.left
                continue
            elif current.val < smaller:
                current = current.right
                continue
            break;

        return current
