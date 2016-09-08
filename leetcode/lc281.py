class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.list_pair = (v1, v2)
        self.indexes = [0, 0]
        self.select = 0
        

    def next(self):
        """
        :rtype: int
        """
        if self.indexes[self.select] >= len(self.list_pair[self.select]):
            self.select = 1 - self.select
        rv = self.list_pair[self.select][self.indexes[self.select]]
        self.indexes[self.select] += 1
        self.select = 1 - self.select
        return rv
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.indexes[0] < len(self.list_pair[0]) or self.indexes[1] < len(self.list_pair[1])


def test():
    def retrieve_all(zi):
        x = []
        while zi.hasNext():
            x.append(zi.next())
        return x

    assert retrieve_all(ZigzagIterator([1,2],[3,4,5,6])) == [1,3,2,4,5,6]
    assert retrieve_all(ZigzagIterator([],[3,4,5,6])) == [3,4,5,6]
    assert retrieve_all(ZigzagIterator([3,4,5,6],[])) == [3,4,5,6]
