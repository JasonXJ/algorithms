from bisect import bisect
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        start_index = sorted((x.start, i) for i, x in enumerate(intervals))
        start_index.append((float('+inf'), -1))
        return [start_index[bisect(start_index, (x.end, -1))][1] for x in intervals]
