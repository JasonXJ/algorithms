class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        graph = [[i, set()] for i in range(n)]
        for v1, v2 in edges:
            graph[v1][1].add(v2)
            graph[v2][1].add(v1)

        interesting_nodes_lists = [[], []]
        interesting_nodes_list_index = 0
        
        for node in graph:
            if len(node[1]) == 1:
                interesting_nodes_lists[0].append(node)

        deleted_node = 0
        while deleted_node != n:
            lst = interesting_nodes_lists[interesting_nodes_list_index]
            lst2 = interesting_nodes_lists[1-interesting_nodes_list_index]
            del lst2[:]
            assert lst, 'error'
            for node_id, neighbours in lst:
                for neighbour_id in neighbours:
                    graph[neighbour_id][1].remove(node_id)
                    if len(graph[neighbour_id][1]) == 1:
                        lst2.append(graph[neighbour_id])
                deleted_node += 1
            interesting_nodes_list_index = 1 - interesting_nodes_list_index

        return [node[0] for node in interesting_nodes_lists[1-interesting_nodes_list_index]]

if __name__ == "__main__":
    print(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
