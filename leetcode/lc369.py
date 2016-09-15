# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) time and O(1) space
class Solution(object):
    def plusOne(self, head):
        helmet = ListNode(0)
        helmet.next = head
        i = helmet
        j = head
        while j is not None:
            if j.val < 9:
                i = j
            j = j.next
        i.val += 1
        i = i.next
        while i is not None:
            i.val = 0
            i = i.next
        if helmet.val != 0:
            return helmet
        return head


# O(n) time/space recursive
class Solution2(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recursive(node):
            if node == None:
                return True
            else:
                if recursive(node.next):
                    node.val += 1
                    if node.val >= 10:
                        node.val -= 10
                        return True
            return False
        

        if recursive(head):
            new_head = ListNode(1)
            new_head.next = head
            return new_head
        else:
            return head
