# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        assert root is not None
        node = root
        different = float('+inf')
        rv = None
        while node is not None:
            if node.val == target:
                return node.val
            new_different = abs(node.val - target)
            if new_different < different:
                different = new_different
                rv = node.val
            if node.val < target:
                node = node.right
            else:
                node = node.left

        return rv
