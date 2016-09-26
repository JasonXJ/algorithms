# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        assert m <= n
        if m == n:
            return head

        dummy = ListNode(None)
        dummy.next = head

        before_m = dummy
        for _ in range(m - 1):
            before_m = before_m.next

        pre_cursor = before_m.next
        cursor = pre_cursor.next
        cursor_index = m + 1
        while cursor_index <= n:
            pre_cursor.next = cursor.next
            cursor.next = before_m.next
            before_m.next = cursor
            cursor = pre_cursor.next
            cursor_index += 1

        return dummy.next
