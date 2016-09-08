from bisect import bisect
from collections import namedtuple
from heapq import heappush, heappop


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        # The process is like tiling. And we always start from the left most
        # and bottom most rectangle.

        # First sort the rectangles. Note that each rectangle is [x1, y1, x2,
        # y2], where x2 > x1 and y2 > y1.
        rectangles.sort()
        x_range_lower = rectangles[0][0]
        y_range_lower = rectangles[0][1]
        y_range_higher = rectangles[
            bisect(rectangles, [x_range_lower, float('inf'), 0, 0]) - 1
        ][3]
        assert y_range_lower < y_range_higher

        # Each element ``(x, y_1, y_2)`` represent a piece of empty rectangle
        # (left-bottom point is (x, y_1), and right-top point is (+inf, y_2))
        # space needed to be filled.
        space_min_heap = [(x_range_lower, y_range_lower, y_range_higher)]


        def get_space():
            assert len(space_min_heap)
            space = list(heappop(space_min_heap))
            while (len(space_min_heap) and
                   space[0] == space_min_heap[0][0] and
                   space[2] == space_min_heap[0][1]):
                # Merge the space
                space[2] = heappop(space_min_heap)[2]
            return tuple(space)


        for x1, y1, x2, y2 in rectangles:
            assert x1 < x2 and y1 < y2
            space_x, space_y1, space_y2 = get_space()
            if x1 != space_x or y1 != space_y1 or y2 > space_y2:
                return False
            heappush(space_min_heap, (x2, y1, y2))
            if y2 < space_y2:
                heappush(space_min_heap, (x1, y2, space_y2))

        final_space = get_space()
        return len(space_min_heap) == 0


def test():
    assert Solution().isRectangleCover([
        [1,1,3,3],
        [3,1,4,2],
        [3,2,4,4],
        [1,3,2,4],
        [2,3,3,4]
    ])

    assert Solution().isRectangleCover([
        [1,1,2,3],
        [1,3,2,4],
        [3,1,4,2],
        [3,2,4,4]
    ]) == False

    assert Solution().isRectangleCover([
        [1,1,3,3],
        [3,1,4,2],
        [1,3,2,4],
        [3,2,4,4]
    ]) == False

    assert Solution().isRectangleCover([
        [1,1,3,3],
        [3,1,4,2],
        [1,3,2,4],
        [2,2,4,4]
    ]) == False

    assert Solution().isRectangleCover([
        [0,0,2,2],
        [0,2,3,3],
    ]) == False

    assert Solution().isRectangleCover([
        [0,0,2,2],
        [0,2,2,3],
    ]) == True

    assert Solution().isRectangleCover([
        [0,0,2,2],
        [0,2,1,3],
    ]) == False
    
    assert Solution().isRectangleCover([
        [0,0,2,3],
        [0,2,2,5],
    ]) == False
    
    assert Solution().isRectangleCover([
        [0,0,2,3],
        [1,3,2,5],
    ]) == False
    
    assert Solution().isRectangleCover([
        [1,0,2,3],
        [0,3,2,5],
    ]) == False
    
