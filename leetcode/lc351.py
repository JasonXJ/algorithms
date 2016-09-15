class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        block_relations = {
            2: [(1,3)],
            4: [(1,7)],
            5: [(1,9),(2,8),(3,7),(4,6)],
            6: [(3,9)],
            8: [(7,9)],
        }
        disallowed_edges = {(x,y) for lst in block_relations.values() for (x,y) in lst}
        edge_matrix = [[0] * 10 for _ in range(10)]
        for i in range(1, 10):
            edge_matrix[0][i] = 1
            for j in range(i + 1, 10):
                if (i, j) not in disallowed_edges:
                    edge_matrix[i][j] = edge_matrix[j][i] = 1

        visited = [True] + [False] * 9
        self.rv = 0
        def backtracking(node=0, depth=0):
            if depth >= m:
                self.rv += 1
            if depth == n:
                return
            for i in range(1, 10):
                if edge_matrix[node][i] == 1 and visited[i] == False:
                    visited[i] = True
                    if i in block_relations:
                        for u, v in block_relations[i]:
                            edge_matrix[u][v] = edge_matrix[v][u] = 1
                    backtracking(i, depth + 1)
                    visited[i] = False
                    if i in block_relations:
                        for u, v in block_relations[i]:
                            edge_matrix[u][v] = edge_matrix[v][u] = 0

        backtracking()
        return self.rv


def test():
    assert Solution().numberOfPatterns(1,1) == 9
    assert Solution().numberOfPatterns(2,2) == 56
    assert Solution().numberOfPatterns(3,3) == 320
    assert Solution().numberOfPatterns(2,3) == 376
    assert Solution().numberOfPatterns(2,9) == 389488
