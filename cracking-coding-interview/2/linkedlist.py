class LinkedList:
    """ A double linked list. """
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self._prev = prev
            self._next = next

        @property
        def prev(self):
            return self._prev
        @property
        def next(self):
            return self._next

        def __iter__(self):
            """ Iterate through this node and the nodes after it in order. """
            current_node = self
            while current_node is not None:
                yield current_node
                current_node = current_node._next

        def __reversed__(self):
            """ Iterate through this node and the nodes before it in reversed order. """
            current_node = self
            while current_node is not None:
                yield current_node
                current_node = current_node._prev

        def __str__(self):
            return "*{}*".format(self.data)

    def __init__(self, *values):
        self._head = None
        self._tail = None

        for data in values:
            self.insert(None, data)

    @property
    def head(self):
        return self._head
    @property
    def tail(self):
        return self._tail

    def insert(self, node, data):
        """ Insert a new node with `data` before `node`. If ``node is None``,
        the new node will be inserted at the end of the list. """
        if node is None:
            # insert after the tail
            if self._tail is None:
                assert self._head is None
                self._head = self._tail = self.Node(data)
            else:
                new_node = self.Node(data, self._tail, None)
                self._tail._next = new_node
                self._tail = new_node
        else:
            new_node = self.Node(data, node._prev, node)
            node._prev = new_node
            if new_node._prev is None:
                assert node is self._head
                self._head = new_node
            else:
                new_node._prev._next = new_node

    def delete(self, node):
        p_node = node._prev
        n_node = node._next

        if p_node is None:
            assert node is self._head
            self._head = n_node
        else:
            p_node._next = n_node

        if n_node is None:
            assert node is self._tail
            self._tail = p_node
        else:
            n_node._prev = p_node

    def __iter__(self):
        if self._head is None:
            assert self._tail is None
        else:
            yield from self._head

    def __reversed__(self):
        if self._tail is None:
            assert self._head is None
        else:
            yield from reversed(self._tail)

    def __repr__(self):
        if self._head is None:
            assert self._tail is None
            return 'LinkedList()'
        else:
            iterator = iter(self)
            string = 'LinkedList(' + str(next(iterator).data)
            for node in iterator:
                string += ', ' + str(node.data)
            string += ')'

        return string

if __name__ == '__main__':
    llist = LinkedList(1,2,3); print(llist)
    # try reversed
    print('reversed:', [x.data for x in reversed(llist)])
    # try delete
    llist.delete(llist._head); print(llist)
    llist.delete(llist._tail); print(llist)
    llist.delete(llist._tail); print(llist)
    # try insert again
    llist.insert(None, 3); print(llist)
    llist.insert(llist._head, 1); print(llist)
    llist.insert(llist._tail, 2); print(llist)
    # delete again (begin from center)
    llist.delete(llist._head._next); print(llist)
    llist.delete(llist._head); print(llist)
    llist.delete(llist._head); print(llist)
