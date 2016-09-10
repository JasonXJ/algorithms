from heapq import heappush, heappop

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# O(n log n) based on heap
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x:x.start)
        end_time_min_heap = []
        required_rooms = 0
        for interval in intervals:
            while len(end_time_min_heap) and end_time_min_heap[0] <= interval.start:
                heappop(end_time_min_heap)
            heappush(end_time_min_heap, interval.end)
            if len(end_time_min_heap) > required_rooms:
                required_rooms = len(end_time_min_heap)

        return required_rooms
