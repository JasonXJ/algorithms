# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        columns = {}
        q = deque()
        q.append((root, 0))
        while len(q):
            node, column = q.popleft()
            if node is None:
                continue
            columns.setdefault(column, []).append(node.val)
            q.append((node.left, column - 1))
            q.append((node.right, column + 1))
        
        return [lst for _, lst in sorted(columns.items())]
