class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        cursor = self
        string = ''
        while cursor != None:
            string += '{}, '.format(cursor.val)
            cursor = cursor.next
        return '[' + string + ']'

def list_to_linked_list(lst):
    cursor = fake_head = ListNode(None)
    for x in lst:
        cursor.next = ListNode(x)
        cursor = cursor.next
    return fake_head.next
