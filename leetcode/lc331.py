class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        child_slots = 1
        index = 0
        while index < len(preorder):
            if child_slots <= 0:
                return False
            if preorder[index] == '#':
                child_slots -= 1
            else:
                child_slots += 1
            index += 1
            while index < len(preorder) and preorder[index] != ',':
                index += 1
            index += 1

        return child_slots == 0
