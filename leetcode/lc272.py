# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# This is an O(min(k log n, n)) solution.
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if root is None or k == 0:
            return []

        RIGHT_DUMMY = TreeNode(float('+inf'))
        LEFT_DUMMY = TreeNode(float('-inf'))

        def move_to_successor(stack):
            if stack[-1] is RIGHT_DUMMY:
                return

            cursor = stack[-1]
            if cursor.right is not None:
                # Find the leftmost node of the right subtree.
                cursor = cursor.right
                stack.append(cursor)
                while cursor.left is not None:
                    cursor = cursor.left
                    stack.append(cursor)
                return stack[-1]
            else:
                # The successor is an ancestor.
                last_top = stack.pop()
                while stack[-1] is not RIGHT_DUMMY:
                    if stack[-1].left is last_top:
                        return
                    last_top = stack.pop()


        def move_to_predecessor(stack):
            if stack[-1] is LEFT_DUMMY:
                return

            cursor = stack[-1]
            if cursor.left is not None:
                # Find the right most node of the left subtree.
                cursor = cursor.left
                stack.append(cursor)
                while cursor.right is not None:
                    cursor = cursor.right
                    stack.append(cursor)
                return
            else:
                # The predecessor is an ancestor.
                last_top = stack.pop()
                while stack[-1] is not LEFT_DUMMY:
                    if stack[-1].right is last_top:
                        return
                    last_top = stack.pop()
                

        # First we find 1) the left-most node `right` such that `right.val >=
        # target` and 2) the right-most node `left` such that ``left.val <
        # target``.
        left = None
        right = None
        cursor = root
        stack = []
        while cursor is not None:
            stack.append(cursor)
            if cursor.val >= target:
                right = cursor
                cursor = cursor.left
            else:  # cursor.val < target
                left = cursor
                cursor = cursor.right

        # Reconstruct stacks
        left_stack = [LEFT_DUMMY]
        right_stack = [RIGHT_DUMMY]
        for selected_stack, stop_node in [(left_stack, left), (right_stack, right)]:
            if stop_node is None:
                continue
            for x in stack:
                selected_stack.append(x)
                if x is stop_node:
                    break

        # Now, we collect the k values one by one by comparing `left_stack[-1].val` and
        # `right_stack[-1].val`
        rv = []
        while len(rv) < k:
            if target - left_stack[-1].val < right_stack[-1].val - target:
                rv.append(left_stack[-1].val)
                move_to_predecessor(left_stack)
            else:
                rv.append(right_stack[-1].val)
                move_to_successor(right_stack)

        return rv


if __name__ == "__main__":
    from binarytree import *
    tree = from_list([10, 1, 20])
    print(Solution().closestKValues(tree, 0.0, 2))
