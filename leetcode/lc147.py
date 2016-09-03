# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(None)
        fake_head.next = head
        previous = fake_head
        current = head
        while current is not None:
            cursor_prev = fake_head
            cursor = fake_head.next
            while cursor != current and cursor.val <= current.val:
                cursor_prev = cursor
                cursor = cursor.next
            if cursor != current:
                # Delete `current`
                previous.next = current.next
                # Insert `current`
                current.next = cursor
                cursor_prev.next = current
                current = previous.next
            else:
                previous = current
                current = current.next

        return fake_head.next


if __name__ == "__main__":
    from linkedlist import *
    llist = list_to_linked_list([5,1,1])
    print(llist)
    print(Solution().insertionSortList(llist))
