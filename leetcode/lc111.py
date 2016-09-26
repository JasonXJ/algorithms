# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        current_nodes = [root]
        next_nodes = []
        depth = 1
        while True:
            for n in current_nodes:
                if n.left is None and n.right is None:
                    return depth
                if n.left is not None:
                    next_nodes.append(n.left)
                if n.right is not None:
                    next_nodes.append(n.right)
            current_nodes, next_nodes = next_nodes, []
            depth += 1
