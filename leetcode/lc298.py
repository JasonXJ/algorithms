from collections import namedtuple
from heapq import heappush, heappop

ValueComplex = namedtuple('ValueComplex', 'key, building')

class Solution(object):
    def getSkyline(self, buildings):
        right_min_heap = []
        height_max_heap = []
        rv = [[-1,-1]]
        building_index = 0
        INF = float('inf')

        def add_to_heaps(building):
            heappush(height_max_heap, ValueComplex(-building[2], building))
            heappush(right_min_heap, ValueComplex(building[1], building))


        # Loop invariant:
        # 1. All elements in `height_max_heap` with a right edge smaller than
        #    or equal to `cursor` is invalid and can just be ignored.
        # 2. Every element in `right_min_heap` has a corresponding valid
        #    element in `height_max_heap`
        # 3. `height_max_heap[0]`, if exists, must be valid and equal to rv[-1][1]
        while True:
            if building_index >= len(buildings) and len(right_min_heap) == 0:
                break

            cursor = INF
            if building_index < len(buildings):
                cursor = buildings[building_index][0]
            if len(right_min_heap):
                cursor = min(cursor, right_min_heap[0].building[1])

            # Process all right edges with the value of `cursor`
            while len(right_min_heap) and right_min_heap[0].building[1] == cursor:
                heappop(right_min_heap)
            # Note that ideally, we would want to remove all the element in
            # `height_max_heap` with a right edge located at `cursor` now.
            # However, standard heap does not support such an operation
            # (although we can write our custom heap).  So, instead, we
            # will leave these invalid elements in the heap and just ignore
            # them next time we meet them by using the current value of
            # `cursor`.
            while len(height_max_heap) and height_max_heap[0].building[1] <= cursor:
                heappop(height_max_heap)

            # Process all new buildings with a left edge at `cursor`.
            while building_index < len(buildings) and buildings[building_index][0] == cursor:
                add_to_heaps(buildings[building_index])
                building_index += 1
            
            new_highest = 0
            if len(height_max_heap):
                new_highest = height_max_heap[0].building[2]

            if new_highest != rv[-1][1]:
                rv.append([cursor, new_highest])

        del rv[0]
        return rv


def test():
    assert (
        Solution().getSkyline([
            [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]
        ]) ==
        [[2,10], [3,15], [7,12], [12,0], [15,10], [20,8], [24,0]]
    )
    assert (
        Solution().getSkyline([
            [0,3,1], [2,3,2], [4,5,1]
        ]) ==
        [[0,1], [2,2], [3,0], [4,1], [5,0]]
    )
    assert (
        Solution().getSkyline([
            [0,3,2],[1,4,1],[2,3,3],[4,5,1]
        ]) ==
        [[0,2],[2,3],[3,1],[5,0]]
    )
    assert (
        Solution().getSkyline([
            [1,3,3],[2,3,1],[3,4,3],[3,5,4]
        ]) ==
        [[1,3],[3,4],[5,0]]
    )
    assert (
        Solution().getSkyline([
            [1,2,1],[1,2,2],[1,2,3]
        ]) ==
        [[1,3],[2,0]]
    )


if __name__ == "__main__":
    import ipdb
    ipdb.set_trace()
    test()
