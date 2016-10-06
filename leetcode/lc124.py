# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SimplifiedSolution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None

        
        self.rv = float('-INF')

        def simple_path_sum(node):
            # This function return the maximum simple path sum starting from
            # the current node. A simple path can only go from the parent to a
            # child. If one of the paths (not necessarily a simple path) whose
            # "highest" node is the current node and it has a path larger than
            # `self.rv`,  `self.rv` will be changed.

            if node is None:
                return 0
            left_simple_path_sum = simple_path_sum(node.left) + node.val
            right_simple_path_sum = simple_path_sum(node.right) + node.val
            max_path_sum = max(left_simple_path_sum + right_simple_path_sum - node.val,
                               left_simple_path_sum,
                               right_simple_path_sum)
            if max_path_sum > self.rv:
                self.rv = max_path_sum

            return max(left_simple_path_sum, right_simple_path_sum, 0)


        simple_path_sum(root)
        return self.rv



class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None


        def populate_simple_path_sum(node):
            if node is None:
                return 0
            node._from_left = max(populate_simple_path_sum(node.left), 0) + node.val
            node._from_right = max(populate_simple_path_sum(node.right), 0) + node.val
            return max(node._from_left, node._from_right)


        def max_path_sum(node):
            max_ = max(node._from_left + node._from_right - node.val,
                       node._from_left, node._from_right)
            if node.left is not None:
                max_ = max(max_, max_path_sum(node.left))
            if node.right is not None:
                max_ = max(max_, max_path_sum(node.right))

            return max_


        populate_simple_path_sum(root)
        return max_path_sum(root)
