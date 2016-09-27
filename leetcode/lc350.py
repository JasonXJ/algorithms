from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        rv = []
        for x, c in c1.items():
            rv.extend([x] * min(c, c2[x]))

        return rv


def test():
    assert Solution().intersect([1,2,2,1], [2,2]) == [2,2]
    assert Solution().intersect([1,2,2,3,1], [2,2]) == [2,2]
