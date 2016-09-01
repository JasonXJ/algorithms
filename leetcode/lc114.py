class Solution(object):
    def flatten(self, root):
        def _flatten(root):
            if root is None:
                return
            left_tail = _flatten(root.left)
            right_tail = _flatten(root.right)
            if left_tail is not None:
                left_tail.right = root.right
                root.right = root.left
                root.left = None

            if right_tail is None:
                if left_tail is None:  # Both left and right are None
                    return root
                else:
                    return left_tail
            return right_tail

        _flatten(root)
