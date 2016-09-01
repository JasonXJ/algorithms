class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return

        fake_head = ListNode(None)
        fake_head.next = head

        anchor = fake_head
        while anchor.next != None:
            cursor = anchor.next
            cursor2 = cursor.next
            while cursor2 != None and cursor2.val == cursor.val:
                cursor2 = cursor2.next
            if cursor.next != cursor2:  # Duplicate
                anchor.next = cursor2
            else:
                anchor = cursor

        return fake_head.next
