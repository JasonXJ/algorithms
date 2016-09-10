# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.rv = None
        def inorder(node, known_smaller = 0):
            if node is None:
                return 0
            assert known_smaller < k
            left_tree_size = inorder(node.left, known_smaller)
            if self.rv is not None:
                return
            if left_tree_size + known_smaller + 1 == k:
                self.rv = node.val
                return
            right_tree_size = inorder(node.right, known_smaller + left_tree_size + 1)
            if self.rv is not None:
                return
            return left_tree_size + right_tree_size + 1
        
        inorder(root)
        return self.rv
