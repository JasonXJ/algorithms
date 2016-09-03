# An binary indexed tree implementation. For binary indexed tree, see
# https://en.wikipedia.org/wiki/Fenwick_tree and
# http://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.bit = [0] * (len(nums) + 1)
        self.vals = [0] * (len(nums) + 1)
        for i, x in enumerate(nums, 0):
            self.update(i, x)


    @staticmethod
    def LSB(val):
        return val & (-val)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        internal_index = i + 1
        difference = val - self.vals[internal_index]
        self.vals[internal_index] = val
        while internal_index < len(self.bit):
            self.bit[internal_index] += difference
            internal_index += self.LSB(internal_index)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefixSum(j) - self.prefixSum(i-1)


    def prefixSum(self, i):
        internal_index = i + 1
        s = 0
        while internal_index != 0:
            s += self.bit[internal_index]
            internal_index -= self.LSB(internal_index)

        return s


def test():
    na = NumArray([1,3,5])
    assert na.sumRange(0,2) == 9
    assert na.sumRange(1,2) == 8
    assert na.sumRange(0,0) == 1
    na.update(1,2)
    assert na.sumRange(0,2) == 8
    assert na.sumRange(1,2) == 7
    assert na.sumRange(0,0) == 1
    na.update(2,-5)
    assert na.sumRange(0,2) == -2
    assert na.sumRange(1,2) == -3
    assert na.sumRange(0,0) == 1
