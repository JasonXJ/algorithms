# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from random import randint


# Reservoir sampling. See https://en.wikipedia.org/wiki/Reservoir_sampling .
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count = 1
        node = self.head
        while node is not None:
            if randint(1, count) == 1:
                rv = node.val
            count += 1
            node = node.next
        return rv
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
