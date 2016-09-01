class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x:x.start)
        merged = [intervals[0]]
        head = merged[0]
        for x in intervals[1:]:
            if x.start > head.end:  # New interval
                merged.append(x)
                head = x
            elif x.end > head.end:
                head.end = x.end

        return merged

class Interval(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __eq__(self, x):
        return self.start == x.start and self.end == x.end

def test():
    f = Solution().merge
    i = Interval
    assert f([i(1, 3), i(2, 6), i(8, 10), i(15, 18)]) == [i(1, 6), i(8, 10), i(15, 18)]
