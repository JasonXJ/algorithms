class Solution(object):
    def reorderList(self, head):
        if head is None:
            return None

        node_list = []
        cursor = head
        while cursor is not None:
            node_list.append(cursor)
            cursor = cursor.next

        left = 0
        right = len(node_list) - 1
        fake_head = ListNode(None)
        cursor = fake_head
        while right > left:
            cursor.next = node_list[left]
            cursor.next.next = node_list[right]
            cursor = cursor.next.next
            left += 1
            right -= 1
        if left == right:
            cursor.next = node_list[left]
            cursor = cursor.next

        cursor.next = None
