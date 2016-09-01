class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # Use DFS for topological sort
        order = []

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
            order.append(node['id'])

        graph = [{'id': i, 'neighbours':[], 'color':'w'} for i in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]]['neighbours'].append(graph[edge[0]])

        try:
            for node in graph:
                if node['color'] == 'w':
                    dfs_visit(node)
        except CycleFound:
            return []

        order.reverse()
        return order
