class LRUCache(object):

    class LinkedList(object):
        class Node:
            def __init__(self, key):
                self.key = key
                self.next = None
                self.prev = None


        def __init__(self):
            self.head = None
            self.tail = None


        def append(self, key):
            new_node = self.Node(key)
            if self.tail is None:
                assert self.head is None
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            return new_node


        def remove_head(self):
            if self.head is None:
                raise RuntimeError
            ori_head_key = self.head.key
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None

            return ori_head_key



        def remove(self, node):
            if node is self.head:
                self.remove_head()
            else:
                # ``node.prev`` must exist.
                node.prev.next = node.next
                if node is not self.tail:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev


        def move_to_end(self, node):
            if node is self.tail:
                return node
            else:
                self.remove(node)
                return self.append(node.key)


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # key -> (value, linked_list_node)
        self.entry_map = {}
        self.linked_list = self.LinkedList()
        self.capacity = capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        complex_value = self.entry_map.get(key)
        if complex_value is None:
            return -1
        else:
            value, node = complex_value
            node = self.linked_list.move_to_end(node)
            self.entry_map[key] = (value, node)
            return value


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        complex_value = self.entry_map.get(key)
        if complex_value is None:
            # Insert new value

            if len(self.entry_map) == self.capacity:
                removed_key = self.linked_list.remove_head()
                del self.entry_map[removed_key]
            node = self.linked_list.append(key)
            self.entry_map[key] = (value, node)
        else:
            node = self.linked_list.move_to_end(complex_value[1])
            self.entry_map[key] = (value, node)



def test():
    cache = LRUCache(2)
    assert cache.get(1) == -1
    cache.set(1, 101)
    assert cache.get(1) == 101
    cache.set(2, 102)
    assert cache.get(1) == 101 and cache.get(2) == 102
    cache.set(2, 1002)
    assert cache.get(1) == 101 and cache.get(2) == 1002
    cache.set(3, 103)
    assert cache.get(1) == -1 and cache.get(2) == 1002 and cache.get(3) == 103
    cache.set(4, 104)
    assert cache.get(2) == -1 and cache.get(3) == 103 and cache.get(4) == 104
    cache.set(3, 1003)
    assert cache.get(4) == 104 and cache.get(3) == 1003
    cache.set(5, 105)
    assert cache.get(4) == -1 and cache.get(3) == 1003 and cache.get(5) == 105
    cache.get(3)  # Get also update the time information
    cache.set(6, 106)
    assert cache.get(5) == -1 and cache.get(3) == 1003 and cache.get(6) == 106
