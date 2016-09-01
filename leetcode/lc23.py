class Solution(object):
    def mergeKLists(self, lists):
        from heapq import heapify, heappush, heappop
        lists = lists[:]  # Avoid changing the original list
        heads_heap = [(lists[i].val, i) for i in range(len(lists)) if lists[i] is not None]
        heapify(heads_heap)
        
        rv = []
        while len(heads_heap) > 0:
            val, i = heappop(heads_heap)
            rv.append(val)
            lists[i] = next_node = lists[i].next
            if next_node is not None:
                heappush(heads_heap, (next_node.val, i))

        return rv
