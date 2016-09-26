class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if k == 0:
            return head
        lastnode = head
        node_count = 1
        while lastnode.next is not None:
            lastnode = lastnode.next
            node_count += 1
        k %= node_count
        if k == 0:
            return head

        pk = head
        for _ in range(node_count - k - 1):
            pk = pk.next
        new_head = pk.next
        pk.next = None
        lastnode.next = head

        return new_head
