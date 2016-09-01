# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        promote = 0
        placeholder_head = ListNode(None)
        cursor = placeholder_head
        c1 = l1
        c2 = l2
        while c1 is not None or c2 is not None or promote != 0:
            v1 = v2 = 0
            if c1 is not None:
                v1 = c1.val
                c1 = c1.next
            if c2 is not None:
                v2 = c2.val
                c2 = c2.next
            v = v1 + v2 + promote
            if v >= 10:
                promote = 1
                v -= 10
            else:
                promote = 0
            cursor.next = ListNode(v)
            cursor = cursor.next

        return placeholder_head.next
