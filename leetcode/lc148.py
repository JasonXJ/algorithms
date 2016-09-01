# An mergesort O(nlogn) time and O(1) space 
class Solution(object):
    def sortList(self, head):
        if head is None:
            return

        def merge_lists(head1, end1, head2, end2):
            fake_head = ListNode(None)
            current = fake_head
            while True:
                if head1.val <= head2.val:
                    current.next = head1
                    if head1 == end1:
                        head1.next = head2
                        return fake_head.next, end2
                    head1 = head1.next
                else:
                    current.next = head2
                    if head2 == end2:
                        head2.next = head1
                        return fake_head.next, end1
                    head2 = head2.next
                current = current.next

        def recursive(first, last):
            if first == last:
                return first, last
            # Search the middle element
            cursor_slow = cursor_fast = first
            i = 0
            while cursor_fast != last:
                cursor_fast = cursor_fast.next
                if i & 0x1:
                    cursor_slow = cursor_slow.next
                i += 1
            cursor_slow_next = cursor_slow.next  # Must cache this value before calling `recursive`
            head1, end1 = recursive(first, cursor_slow)
            head2, end2 = recursive(cursor_slow_next, cursor_fast)
            return merge_lists(head1, end1, head2, end2)

        tail = head
        while tail.next != None:
            tail = tail.next
        new_head, new_tail = recursive(head, tail)
        new_tail.next = None
        return new_head

if __name__ == "__main__":
    from linkedlist import *
    print(Solution().sortList(list_to_linked_list([3,2,4])))
