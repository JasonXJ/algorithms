# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._visit_left(root)

    def _visit_left(self, node):
        if node is not None:
            self.stack.append(node)
            self._visit_left(node.left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0
        

    def next(self):
        """
        :rtype: int
        """
        last_node = self.stack.pop()
        self._visit_left(last_node.right)

        return last_node.val
