from linkedlist import LinkedList

def is_palindrome(llist):
    head = llist.head
    tail = llist.tail
    if head is None:
        # Empty list.
        return True
    while head.data == tail.data:
        if head is tail:
            # The length is odd.
            return True
        head = head.next
        if head is tail:
            # The length is even
            return True
        tail = tail.prev
    return False

if __name__ == '__main__':
    print(is_palindrome(LinkedList(1, 2, 3, 2, 1)))
    print(is_palindrome(LinkedList(1, 2, 3, 3, 2, 1)))
    print(is_palindrome(LinkedList()))
    print(is_palindrome(LinkedList(1)))
    print(is_palindrome(LinkedList(1, 1)))
    print(is_palindrome(LinkedList(1, 2)))
    print(is_palindrome(LinkedList(1, 2, 3)))
