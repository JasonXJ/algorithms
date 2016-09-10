# An worst case O(k log mn) solution. Where k is the length of `positions`.
# Note that it is actually O(k log k'), where k' is the number of unique value
# in `positions`. Since k' <= mn, the algorithm is also  O(k log mn).
# 
# P.S. The union-find algorithm used here is effectively the linked-list
# disjoint sets algorithm (see 21.2 of Introduction to Algorithms)
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # Note that we cannot use a whole matrix, which will incur a O(mn)
        # cost.
        pos_to_island_id = {}
        # A mapping from the island id to a list of positions.
        islands = {}
        rv = []

        for row, col in positions:
            if (row, col) in pos_to_island_id:
                continue
            surrounding_island_ids = []
            neighbours = (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1)
            )
            for row2, col2 in neighbours:
                try:
                    surrounding_island_ids.append(pos_to_island_id[(row2, col2)])
                except KeyError:
                    pass
            if len(surrounding_island_ids) == 0:
                # Create a new unique island id
                island_id = len(pos_to_island_id)
                island = islands[island_id] = []
            else:
                island_id = surrounding_island_ids.pop()
                island = islands[island_id]
                # Merge islands
                for island_id2 in surrounding_island_ids:
                    if island_id2 == island_id:
                        continue
                    # Note that we need to check the existence of `island2`
                    # because it might has been merged because
                    # `surrounding_island_ids` can contain duplicated elements.
                    island2 = islands.get(island_id2)
                    if island2 is not None:
                        # Merge the two islands
                        if len(island) < len(island2):
                            island, island2 = island2, island
                            island_id, island_id2 = island_id2, island_id
                        island.extend(island2)
                        for member in island2:
                            pos_to_island_id[member] = island_id
                        del islands[island_id2]
            pos_to_island_id[(row, col)] = island_id
            island.append((row, col))
            rv.append(len(islands))

        return rv


def test():
    assert Solution().numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]]) == [1, 1, 2, 3]
    assert Solution().numIslands2(3, 3, [[0,1], [1,0], [1,2], [2,1], [1,1]]) == [1, 2, 3, 4, 1]
