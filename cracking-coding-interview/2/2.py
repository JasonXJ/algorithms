from linkedlist import LinkedList

def k_to_the_last(llist, k):
    # pretending llist is singly linked
    assert k >= 0

    probe_node = llist.head
    length = 0
    while probe_node is not None:
        probe_node = probe_node.next
        length += 1

    steps = length - k - 1
    if steps >= 0:
        node = llist.head
        for i in range(steps):
            node = node.next
        return node

if __name__ == '__main__':
    print(k_to_the_last(LinkedList(4, 3, 2, 1, 0), 0))
    print(k_to_the_last(LinkedList(4, 3, 2, 1, 0), 1))
    print(k_to_the_last(LinkedList(4, 3, 2, 1, 0), 4))
    print(k_to_the_last(LinkedList(4, 3, 2, 1, 0), 5))
    print(k_to_the_last(LinkedList(4, 3, 2, 1, 0), 5))
    print(k_to_the_last(LinkedList(), 0))
