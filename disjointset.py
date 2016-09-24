from collections import namedtuple


class DisjointSet:
    """ A disjoint set implemented with trees. See Section 21.3 of Introduction
    to Algorithms for details. Note that both heuristics, namely "union by
    rank" and "path compression", are implemented.   """

    class Node:
        def __init__(self, value):
            self.value = value
            self.rank = 0
            self.parent = self


    def __init__(self):
        self.nodes = {}

    
    def makeset(self, val):
        """ Create a new set with `val` as the only member. """
        if val in self.nodes:
            raise ValueError
        self.nodes[val] = self.Node(val)


    def union(self, val1, val2):
        rp1 = self._findset(val1)
        rp2 = self._findset(val2)
        if rp1 is rp2:
            return False
        if rp1.rank < rp2.rank:
            rp1, rp2 = rp2, rp1
        rp2.parent = rp1
        if rp1.rank == rp2.rank:
            rp1.rank += 1
        return True


    def _findset(self, val):
        def find_and_compress(node):
            if node.parent is not node:
                # The current node is not the representative. Recursively find the
                # representative and set `node.parent` to the representative to
                # compress the path.
                node.parent = find_and_compress(node.parent)
            return node.parent


        return find_and_compress(self.nodes[val])


    def findset(self, val):
        return self._findset(val).value



class LinkedListDisjointSet:
    """ A disjoint set implemented with linked list. See Section 21.2 of
    Introduction to Algorithms. Also note that the "weighted-union heuristic"
    is used to improve the efficiency.
    """
    class Node:
        def __init__(self, val):
            self.representative_value = val
            self.next = self
            # The size is only maintained for representatives (i.e. those
            # self.representative_value == val)
            self.size = 1


    def __init__(self):
        self.nodes = {}


    def makeset(self, val):
        """ Create a new set with `val` as the only member. """
        if val in self.nodes:
            raise ValueError
        self.nodes[val] = self.Node(val)


    def union(self, v1, v2):
        """ Return False if the two are already in the same set; otherwise
        union them and return True. """
        rp1val = self.nodes[v1].representative_value
        rp2val = self.nodes[v2].representative_value
        if rp1val != rp2val:
            rp1 = self.nodes[rp1val]
            rp2 = self.nodes[rp2val]
            if rp1.size < rp2.size:
                rp1, rp2 = rp2, rp1
            new_rp_val = rp1.representative_value

            # Update representative
            cursor = rp2.next
            while cursor is not rp2:
                cursor.representative_value = new_rp_val
                cursor = cursor.next
            cursor.representative_value = new_rp_val

            # Link
            ori_rp1_next = rp1.next
            rp1.next = rp2.next
            rp2.next = ori_rp1_next

            # Update other info.
            rp1.size += rp2.size

            return True
        return False
    

    def findset(self, value):
        """ Return the representative. """
        return self.nodes[value].representative_value


def test_LinkedListDisjointSet():
    s = LinkedListDisjointSet()
    for i in range(9):
        s.makeset(i)
    for i in range(9):
        assert s.findset(i) == i

    # Union 0~3
    assert s.union(0, 1)
    assert s.findset(0) == s.findset(1) and s.findset(0) in (0, 1)
    set1 = s.findset(0)
    assert s.union(2, 0)
    assert s.findset(2) == set1, 'The smaller set should be merged into the larger one.'
    assert s.union(1, 3)
    assert s.findset(3) == set1, 'The smaller set should be merged into the larger one.'
    assert s.union(0, 1) == False
    assert s.union(1, 3) == False
    assert s.union(1, 1) == False
    
    # Union 4~8
    assert s.union(4,5)
    assert s.union(6,7)
    set2 = s.findset(6)
    assert s.findset(7) == set2
    assert s.union(7,8)
    assert s.findset(8) == set2 and s.union(6,8) == False
    assert s.union(5,8)
    assert all(s.findset(x) == set2 for x in range(4, 9))
    assert s.union(4,7) == False

    # Union the two set
    assert s.union(1, 7)
    assert all(s.findset(x) == set2 for x in range(9))



def test_DisjointSet():
    s = DisjointSet()
    for i in range(9):
        s.makeset(i)
    for i in range(9):
        assert s.findset(i) == i
        assert s._findset(i).rank == 0

    # Union 0~3
    assert s.union(0, 1)
    assert s.findset(0) == s.findset(1) and s.findset(0) in (0, 1)
    set1 = s.findset(0)
    assert s._findset(set1).rank == 1
    assert s.union(2, 0)
    assert s.findset(2) == set1, 'The lower rank set should be merged into the higher'
    assert s._findset(set1).rank == 1
    assert s.union(1, 3)
    assert s.findset(3) == set1, 'The lower rank set should be merged into the higher'
    assert s._findset(set1).rank == 1
    assert s.union(0, 1) == False
    assert s.union(1, 3) == False
    assert s.union(1, 1) == False
    
    # Union 4~8
    assert s.union(4,5)
    assert s.union(6,7)
    assert s.union(7,8)
    assert s.findset(4) == s.findset(5) != s.findset(6)
    assert s.findset(6) == s.findset(7) == s.findset(8)
    assert s.union(6,8) == False
    assert s._findset(4).rank == 1 and s._findset(6).rank == 1
    assert s.union(5,8)
    set2 = s.findset(5)
    assert all(s.findset(x) == set2 for x in range(4, 9))
    assert s.union(4,7) == False
    assert s._findset(set2).rank == 2

    # Union the two set
    assert s.union(1, 7)
    assert all(s.findset(x) == set2 for x in range(9)), 'The lower rank set should be merged into the higher'
