from bisect import bisect_left

# O(n log n) solution using the longest increasing subsequence algorithm.
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Here we first use a set for deduplication. Then we sort the envelopes
        # in ascending order of width and descending order of height.
        processed_envelopes = sorted({(w, h) for w, h in envelopes},
                                     key=lambda x:(x[0], -x[1]))

        # Find the longest increasing subsequence w.r.t height.
        # The details of this algorithm can be found on
        # https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms .
        # M[i] is the height of the last element of a subsequence of length i +
        # 1. If there are multiple subsequence of length i + 1, then M[i] is
        # the minimum one.
        M = []
        for _, h in processed_envelopes:
            m_index = bisect_left(M, h)
            if m_index == len(M):
                M.append(h)
            elif M[m_index] > h:
                M[m_index] = h

        return len(M)


def test():
    assert Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3
