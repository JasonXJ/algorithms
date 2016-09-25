# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# Similar to `SummaryRanges`, except that the disjoint set data structure is
# not used.
class SimplerSummaryRanges(object):
    def __init__(self):
        self.number_to_representative = {}
        self.range_set = set()
        self.interval_cache = None


    def addNum(self, val):
        if val in self.number_to_representative:
            return
        self.number_to_representative[val] = (val, val)
        self.range_set.add((val, val))
        if val - 1 in self.number_to_representative:
            self._merge(val - 1, val)
        if val + 1 in self.number_to_representative:
            self._merge(val, val + 1)
        self.interval_cache = None


    def _merge(self, val1, val2):
        s1, e1 = self.number_to_representative[val1]
        s2, e2 = self.number_to_representative[val2]
        assert s2 == e1 + 1
        # Only need to update the the start and the end of the new range
        self.number_to_representative[s1] = self.number_to_representative[e2] = (s1, e2)
        self.range_set.remove((s1, e1))
        self.range_set.remove((s2, e2))
        self.range_set.add((s1, e2))
    

    def getIntervals(self):
        if self.interval_cache is None:
            self.interval_cache = sorted(
                (
                    Interval(s, e)
                    for s, e
                    in self.range_set
                ),
                key=lambda i:i.start
            )

        return self.interval_cache



# Disjoint set solution. Note that we use the tree disjoint set with
# union-by-rank and path-compression, which makes the `addNum` method very
# efficient (O(\alpha (n))). However, since the returned intervals is required
# to be sorted, the first time `getIntervals` is called after the new numbers
# are added will cost O(n log n) time. A more efficient way is to use
# self-balanced BST. See `SummaryRanges2` for a more efficient solution which
# does not maintain the order of the values returned by `getIntervals`.
class SummaryRanges(object):
    class DSNode:
        def __init__(self, val):
            self.parent = self
            self.val = val
            self.interval = (val, val)
            self.rank = 0


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = set()
        self.intervals_lst_cache = None
        # Mapping from int -> DSNode
        self.disjointset = {}
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.disjointset:
            return
        node = self.DSNode(val)
        self.disjointset[val] = node
        self.intervals.add(node.interval)
        if val - 1 in self.disjointset:
            self._mergerange(val - 1, val)
        if val + 1 in self.disjointset:
            self._mergerange(val, val + 1)
        self.intervals_lst_cache = None


    def _mergerange(self, val1, val2):
        rp_node1 = self._findset(val1)
        rp_node2 = self._findset(val2)
        assert rp_node1 is not rp_node2
        if rp_node1.rank < rp_node2.rank:
            rp_node1, rp_node2 = rp_node2, rp_node1
        rp_node2.parent = rp_node1
        if rp_node1.rank == rp_node2.rank:
            rp_node1.rank += 1
        self.intervals.remove(rp_node1.interval)
        self.intervals.remove(rp_node2.interval)
        assert (rp_node1.interval[0] == rp_node2.interval[1] + 1 or
                rp_node1.interval[1] + 1 == rp_node2.interval[0])
        rp_node1.interval = (min(rp_node1.interval[0], rp_node2.interval[0]),
                             max(rp_node1.interval[1], rp_node2.interval[1]))
        self.intervals.add(rp_node1.interval)
        return True


    def _findset(self, val):
        node = self.disjointset[val]

        def findset_(node):
            if node.parent is not node:
                node.parent = findset_(node.parent)
            return node.parent

        return findset_(node)
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        if self.intervals_lst_cache is None:
            self.intervals_lst_cache = [
                Interval(start, end)
                for start, end in self.intervals
            ]
            self.intervals_lst_cache.sort(key=lambda i:i.start)
        return self.intervals_lst_cache



# This one is similar to `SummaryRanges` except that an `IntervalKeeper` is used
# so that `addNum` runs in O(\alpha(n)) time and `getIntervals` runs in O(1)
# time. However, `getIntervals` returns the intervals in arbitrary order, so
# this version does not pass leetcode's test.
class SummaryRanges2(object):
    class DSNode:
        def __init__(self, val):
            self.parent = self
            self.val = val
            self.interval = (val, val)
            self.rank = 0


    class IntervalKeeper:
        def __init__(self):
            self.range_to_index = {}
            self.intervals = []


        def add(self, r):
            assert r not in self.range_to_index
            self.range_to_index[r] = len(self.intervals)
            self.intervals.append(Interval(*r))


        def remove(self, r):
            assert r in self.range_to_index
            i = self.range_to_index[r]
            self.intervals[i] = self.intervals[-1]
            self.range_to_index[(self.intervals[i].start, self.intervals[i].end)] = i
            del self.range_to_index[r]
            del self.intervals[-1]


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = self.IntervalKeeper()
        # Mapping from int -> DSNode
        self.disjointset = {}
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.disjointset:
            return
        node = self.DSNode(val)
        self.disjointset[val] = node
        self.intervals.add(node.interval)
        if val - 1 in self.disjointset:
            self._mergerange(val - 1, val)
        if val + 1 in self.disjointset:
            self._mergerange(val, val + 1)
        self.intervals_lst_cache = None


    def _mergerange(self, val1, val2):
        rp_node1 = self._findset(val1)
        rp_node2 = self._findset(val2)
        assert rp_node1 is not rp_node2
        if rp_node1.rank < rp_node2.rank:
            rp_node1, rp_node2 = rp_node2, rp_node1
        rp_node2.parent = rp_node1
        if rp_node1.rank == rp_node2.rank:
            rp_node1.rank += 1
        self.intervals.remove(rp_node1.interval)
        self.intervals.remove(rp_node2.interval)
        assert (rp_node1.interval[0] == rp_node2.interval[1] + 1 or
                rp_node1.interval[1] + 1 == rp_node2.interval[0])
        rp_node1.interval = (min(rp_node1.interval[0], rp_node2.interval[0]),
                             max(rp_node1.interval[1], rp_node2.interval[1]))
        self.intervals.add(rp_node1.interval)
        return True


    def _findset(self, val):
        node = self.disjointset[val]

        def findset_(node):
            if node.parent is not node:
                node.parent = findset_(node.parent)
            return node.parent

        return findset_(node)
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

if __name__ == "__main__":
    sr = SimplerSummaryRanges()
    sr.addNum(1)
    print(sr.getIntervals())
    sr.addNum(3)
    print(sr.getIntervals())
    sr.addNum(7)
    print(sr.getIntervals())
    sr.addNum(2)
    print(sr.getIntervals())
    sr.addNum(6)
    print(sr.getIntervals())
