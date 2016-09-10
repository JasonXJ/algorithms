# O(n) solution
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        max_citation = len(citations)
        citation_counts = [0] * (max_citation + 1)
        for x in citations:
            if x > max_citation:
                x = max_citation
            citation_counts[x] += 1

        hindex = 0
        larger_citation_count = len(citations)
        while hindex < len(citations):
            larger_citation_count -= citation_counts[hindex]
            hindex += 1
            if larger_citation_count < hindex:
                hindex -= 1
                break

        return hindex


def test():
    assert Solution().hIndex([3,0,6,1,5]) == 3
    assert Solution().hIndex([]) == 0
    assert Solution().hIndex([0,0,0,0]) == 0
    assert Solution().hIndex([1,1,1,1]) == 1
    assert Solution().hIndex([3,3]) == 2
    assert Solution().hIndex([3,3,3]) == 3
    assert Solution().hIndex([3,3,3,3]) == 3
    assert Solution().hIndex([4,4,4]) == 3
    assert Solution().hIndex([100,100,100]) == 3
    assert Solution().hIndex([100,100,100]) == 3
