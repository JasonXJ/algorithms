class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        assert len(nums1) + len(nums2) >= k

        if len(nums1) > k:
            nums1 = self.max_subsequence(nums1, k)
        if len(nums2) > k:
            nums2 = self.max_subsequence(nums2, k)
        rv = [-1]
        for seq1_length in range(k - len(nums2), len(nums1) + 1):
            rv2 = self.merge_sequence(self.max_subsequence(nums1, seq1_length),
                                      self.max_subsequence(nums2, k - seq1_length))
            if self.smaller(rv, rv2):
                rv = rv2

        return rv


    def merge_sequence(self, seq1, seq2):
        i1 = i2 = 0
        rv = []
        while i1 < len(seq1) or i2 < len(seq2):
            if self.smaller(seq1, seq2, i1, i2):
                rv.append(seq2[i2])
                i2 += 1
            else:
                rv.append(seq1[i1])
                i1 += 1

        return rv

    
    @staticmethod
    def smaller(seq1, seq2, i1 = 0, i2 = 0):
        while i1 < len(seq1) and i2 < len(seq2):
            if seq1[i1] < seq2[i2]:
                return True
            elif seq1[i1] > seq2[i2]:
                return False
            i1 += 1
            i2 += 1
        # Consider the shorter sequence as smaller.
        return i1 == len(seq1)


    @staticmethod
    def max_subsequence(lst, k):
        assert k <= len(lst)
        if k == len(lst):
            return lst
        elif k == 0:
            return []
        else:
            stack = []
            left = len(lst)
            for x in lst:
                while len(stack) and len(stack) + left > k and stack[-1] < x:
                    stack.pop()
                stack.append(x)
                left -= 1
            return stack[:k]


def test():
    assert Solution().maxNumber([3,4,6,5], [9,1,2,5,8,3], 5) == [9, 8, 6, 5, 3]
    assert Solution().maxNumber([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4]
    assert Solution().maxNumber([6, 7], [6,7,5], 5) == [6, 7, 6, 7, 5]
    assert Solution().maxNumber([6, 7], [6,7,7], 5) == [6, 7, 7, 6, 7]
    assert Solution().maxNumber([3, 9], [8, 9], 3) == [9, 8, 9]
    assert Solution().maxNumber([3,4,5], [], 3) == [3,4,5]
    assert Solution().maxNumber([3], [], 1) == [3]
    assert Solution().maxNumber([3], [1,2], 0) == []
