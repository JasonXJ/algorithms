# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        fake_new_head = RandomListNode(0)
        cursor = head
        new_cursor = fake_new_head
        # Map the id of node in the original list to the corresponding new node
        id_map = {}
        while cursor is not None:
            new_node = RandomListNode(cursor.label)
            id_map[id(cursor)] = new_node
            new_cursor.next = new_node
            cursor = cursor.next
            new_cursor = new_node

        cursor = head
        new_cursor = fake_new_head.next
        while cursor is not None:
            if cursor.random is not None:
                new_cursor.random = id_map[id(cursor.random)]
            cursor = cursor.next
            new_cursor = new_cursor.next

        return fake_new_head.next
