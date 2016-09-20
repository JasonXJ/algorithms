class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [set() for _ in range(n)]
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)

        def dfs(nid):
            if graph[nid] is None:
                return
            node = graph[nid]
            graph[nid] = None
            for nid2 in node:
                dfs(nid2)

        count = 0
        for nid, node in enumerate(graph):
            if node is not None:
                dfs(nid)
                count += 1

        return count
