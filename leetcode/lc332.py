from collections import Counter

class Node:
    def __init__(self, label):
        self.label = label
        self.neighbours = Counter()

class Solution(object):

    class _FinishedException(Exception):
        pass

    def findItinerary(self, tickets):
        label_to_node = {}

        for from_, to_ in tickets:
            if from_ not in label_to_node:
                label_to_node[from_] = Node(from_)
            if to_ not in label_to_node:
                label_to_node[to_] = Node(to_)
            label_to_node[from_].neighbours[label_to_node[to_]] += 1

        rv = ['JFK']
        rv_max_length = len(tickets) + 1

        def search(from_):
            if len(from_.neighbours) == 0:
                if len(rv) == rv_max_length:
                    raise self._FinishedException
                return
            else:
                sorted_neighbours = sorted(from_.neighbours, key=lambda x:x.label)
                for neighbour in sorted_neighbours:
                    rv.append(neighbour.label)
                    count = from_.neighbours[neighbour]
                    if count == 1:
                        del from_.neighbours[neighbour]
                    else:
                        from_.neighbours[neighbour] -= 1

                    search(neighbour)

                    from_.neighbours[neighbour] += 1
                    rv.pop()

        try:
            search(label_to_node['JFK'])
        except self._FinishedException:
            return rv

        assert False, 'error'

if __name__ == "__main__":
    print(Solution().findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
