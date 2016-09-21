class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return list(range(n))
        graph = {i:set() for i in range(n)}
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        lonely_nodes = []
        next_lonely_nodes = []
        for i in range(n):
            if len(graph[i]) == 1:
                lonely_nodes.append(i)

        while len(graph) > 2:
            for x in lonely_nodes:
                neighbour = graph.pop(x).pop()
                graph[neighbour].remove(x)
                if len(graph[neighbour]) == 1:
                    next_lonely_nodes.append(neighbour)
            lonely_nodes, next_lonely_nodes = next_lonely_nodes, []

        return list(graph)


def test():
    def check(n, edges, expected):
        assert sorted(Solution().findMinHeightTrees(n, edges)) == sorted(expected)

    check(4, [[1,0],[1,2],[1,3]], [1])
    check(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]], [3,4])
    check(2, [[0,1]], [0,1])
    check(1, [], [0])
