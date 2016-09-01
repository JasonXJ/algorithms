def _create_list(cls, *args):
    if len(args) == 0:
        return
    head = tail = cls(args[0])
    for x in args[1:]:
        tail.append_to_tail(x)

    return head

class SinglyNode:
    def __init__(self, data=None):
        self.data = data
        self._next = None

    @classmethod
    def create_list(cls, *args):
        """ Create a link list with value specified in `args` and return the
        head node """
        return _create_list(cls, *args)

    def append_to_tail(self, data):
        last_node = self
        while last_node._next is not None:
            last_node = last_node._next
        new_node = SinglyNode(data)
        last_node._next = new_node
        
        return new_node

    def insert_after(self, data):
        new_node = SinglyNode(data)
        new_node._next = self._next
        self._next = new_node

        return new_node

    def __str__(self):
        string = str(self.data)
        last_node = self._next
        while last_node is not None:
            string += ' -> ' + str(last_node.data)
            last_node = last_node._next
        return string

class DoubleNode:
    def __init__(self, data=None):
        self.data = data
        self._next = None
        self._prev = None

    @classmethod
    def create_list(cls, *args):
        """ Create a link list with value specified in `args` and return the
        head node """
        return _create_list(cls, *args)

    def append_to_tail(self, data):
        last_node = self
        while last_node._next is not None:
            last_node = last_node._next

        return last_node.insert_after(data)

    def insert(self, data):
        new_node = DoubleNode(data)
        new_node._next = self
        new_node._prev = self._prev
        self._prev = new_node
        if new_node._prev is not None:
            new_node._prev._next = new_node

        return new_node
    
    def insert_after(self, data):
        new_node = DoubleNode(data)
        new_node._prev = self
        new_node._next = self._next
        self._next = new_node
        if new_node._next is not None:
            new_node._next._prev = new_node

        return new_node

    def __str__(self):
        # Find the first node.
        current_node = self
        while current_node._prev is not None:
            current_node = current_node._prev

        string = str(current_node.data)
        while current_node._next is not None:
            current_node = current_node._next
            string += ' <-> ' + str(current_node.data)

        return string

if __name__ == '__main__':
    link_list = SinglyNode(1)
    n2 = link_list.append_to_tail(2)
    n3 = link_list.append_to_tail(3)
    n4 = link_list.append_to_tail(4)

    n2.insert_after(2.5)
    n3.insert_after(3.5)
    n4.insert_after(4.5)

    print(link_list)

    link_list_with_head = SinglyNode('HEAD')
    na = link_list_with_head.append_to_tail('a')
    nb = link_list_with_head.append_to_tail('b')
    nc = link_list_with_head.append_to_tail('c')
    nd = link_list_with_head.append_to_tail('d')

    link_list_with_head.insert_after('Z')
    print(link_list_with_head)

    double_linked_list = DoubleNode(1)
    dn0 = double_linked_list.insert(0)
    dn2 = double_linked_list.insert_after(2)
    dn3 = dn2.insert_after(3)
    dn2_5 = dn3.insert(2.5)
    dn2_2 = dn2.insert_after(2.2)

    print(dn3)
