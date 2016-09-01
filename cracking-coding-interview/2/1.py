from linkedlist import LinkedList

def remove_duplicates(llist):
    value_set = set()
    current_node = llist.head
    while current_node is not None:
        if current_node.data in value_set:
            temp_node = current_node
            current_node = current_node.next
            llist.delete(temp_node)
        else:
            value_set.add(current_node.data)
            current_node = current_node.next

def remove_duplicates__save_space(llist):
    test_node = llist.head
    while test_node is not None:
        probe_node = test_node.next
        while probe_node is not None:
            if probe_node.data == test_node.data:
                temp_node = probe_node
                probe_node = probe_node.next
                llist.delete(temp_node)
        test_node = test_node.next

def remove_and_print(llist):
    print(llist, end=' => ')
    remove_duplicates(llist)
    print(llist)

def remove_and_print__save_space(llist):
    print(llist, end=' => ')
    remove_duplicates(llist)
    print(llist)

if __name__ == '__main__':
    remove_and_print(LinkedList(1, 2, 3, 2, 3, 4, 5, 5))
    remove_and_print(LinkedList(1, 1, 2, 3, 2, 3, 4, 5, 5, 6))

    remove_and_print__save_space(LinkedList(1, 2, 3, 2, 3, 4, 5, 5))
    remove_and_print__save_space(LinkedList(1, 1, 2, 3, 2, 3, 4, 5, 5, 6))
