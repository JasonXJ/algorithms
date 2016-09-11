class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # Note that since intervals are sorted by the start times, they are
        # also sorted by the end times.
        l = 0
        r = len(intervals) - 1
        target = newInterval.start
        while l <= r:
            m = (l + r) // 2
            if intervals[m].end < target:
                l = m + 1
            else:
                r = m - 1

        # Now intervals[l:] has an end time that >= newInterval.start and
        # intervals[:l] has an end time that < newInterval.start.
        merge_open_right = l
        while (merge_open_right < len(intervals) and
               intervals[merge_open_right].start <= newInterval.end):
            merge_open_right += 1
        if l < merge_open_right:
            newInterval.start = min(newInterval.start, intervals[l].start)
            newInterval.end = max(newInterval.end, intervals[merge_open_right-1].end)

        return intervals[:l] + [newInterval] + intervals[merge_open_right:]


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def test():
    def check(intervals, new_interval, expected):
        converted_intervals = [
            Interval(start, end)
            for start, end
            in intervals
        ]
        rv = Solution().insert(converted_intervals, Interval(*new_interval))
        converted_rv = [
            (x.start, x.end)
            for x in rv
        ]
        assert converted_rv == expected


    check([(0,1)], (2,3), [(0,1),(2,3)])
    check([(1,3),(6,9)], (2,5), [(1,5),(6,9)])
    check([(1,2),(3,5),(6,7),(8,10),(12,16)], (4,9), [(1,2),(3,10),(12,16)])
    check([], (4,9), [(4,9)])
    check([(0,1),(2,3)], (1,2), [(0,3)])
    check([(1,2), (3,4)], (1,2), [(1,2),(3,4)])
    check([(-1,0), (1,2), (3,4)], (1,2), [(-1,0),(1,2),(3,4)])
    check([(3,4)], (1,2), [(1,2),(3,4)])
