# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.rv = 0
        def visit(node=root, val=0):
            val = 10 * val + node.val
            if node.left is None and node.right is None:
                self.rv += val
            else:
                if node.left is not None:
                    visit(node.left, val)
                if node.right is not None:
                    visit(node.right, val)


        visit()
        return self.rv
