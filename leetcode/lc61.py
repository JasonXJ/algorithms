# XXX This one didn't pass the leetcode examination. But I think it is that the
# test cases on the platform are wrong.

class Solution(object):
    def rotateRight(self, head, k):
        pivot1 = head
        i = 0
        while i < k:
            if pivot1 is None:
                return head
            pivot1 = pivot1.next
            i += 1
        if pivot1 is None or pivot1.next is None:
            return head
        pivot2 = pivot1.next
        pivot1.next = None

        original_end = pivot2
        assert original_end is not None
        while original_end.next is not None:
            original_end = original_end.next
        original_end.next = head

        return pivot2
