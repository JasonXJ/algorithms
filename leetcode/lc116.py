# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# O(n) time and O(1) extra space solution. Note that the binary tree is a
# perfect one, which is the reason why this code works.
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        root.next = None
        parent = root
        left_most_child = root.left

        while left_most_child is not None:
            cursor_left = left_most_child
            while cursor_left is not None:
                if cursor_left is parent.left:
                    cursor_right = parent.right
                else:
                    parent = parent.next
                    cursor_right = parent.left if parent is not None else None
                cursor_left.next = cursor_right
                cursor_left = cursor_right
            parent = left_most_child
            left_most_child = left_most_child.left
