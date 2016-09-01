class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Use DFS to detect if the graph is acyclic.
        class CycleFound(Exception):
            pass
        
        def dfs_visit(node):
            node['color'] = 'g'
            for neighbour in node['neighbours']:
                neighbour_color = neighbour['color']
                if neighbour_color == 'w':
                    dfs_visit(neighbour)
                elif neighbour_color == 'g':
                    raise CycleFound
            node['color'] = 'b'

        graph = [{'neighbours':[], 'color':'w'} for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]]['neighbours'].append(graph[edge[0]])

        try:
            for node in graph:
                if node['color'] == 'w':
                    dfs_visit(node)
        except CycleFound:
            return False

        return True
