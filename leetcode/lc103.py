# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        rv = []
        level = [root]
        next_level = []
        to_right = True

        while level:
            rv.append([])
            if to_right:
                for x in level:
                    rv[-1].append(x.val)
            else:
                for x in reversed(level):
                    rv[-1].append(x.val)
            to_right = not to_right
            for n in level:
                if n.left is not None:
                    next_level.append(n.left)
                if n.right is not None:
                    next_level.append(n.right)
            level, next_level = next_level, []


        return rv
