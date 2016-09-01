from linkedlist import LinkedList

def partition(llist, x):
    current_node = llist.head
    while current_node is not None:
        if current_node.data < x:
            # Move before head
            temp_node = current_node
            current_node = current_node.next
            llist.delete(temp_node)
            llist.insert(llist.head, temp_node.data)
        else:
            current_node = current_node.next

def partition_and_print(llist, x):
    print(llist, end=' => ')
    partition(llist, x)
    print(llist)

if __name__ == '__main__':
    partition_and_print(LinkedList(5,4,3,2,1), 3);
    partition_and_print(LinkedList(0,5,4,3,2,1,6), 3);
    partition_and_print(LinkedList(), 3);
    partition_and_print(LinkedList(2), 3);
    partition_and_print(LinkedList(4), 3);
