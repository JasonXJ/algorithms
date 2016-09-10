# This version did not pass the leetcode test. I think the question is
# confusing and not very good because they want us to copy a UNDIRECTED graph,
# but the representation is for directed graph. For example, for a graph with
# only two nodes: A - B. Their representation only contain an edge from A to B
# and no edge is from B to A. Actually, this makes the problem easier. However,
# I wrote one which handle the "correct" representation, so my code could not
# pass the test. And I don't want to change the code.
class Solution(object):
    @staticmethod
    def printGraph(node):
        visited = set()
        def visit(node):
            visited.add(node)
            print('{}: {}'.format(node.label, [nnode.label for nnode in node.neighbors]))
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visit(neighbor)
        visit(node)

    def cloneGraph(self, node):
        # DFS implementation
        if node is None:
            return

        self.printGraph(node)

        # new_head = UndirectedGraphNode(node.label)
        label_to_node_and_status = {}

        def visit(ori_node):
            node = UndirectedGraphNode(ori_node.label)
            current_node_and_status = [node, 'v']
            label_to_node_and_status[ori_node.label] = current_node_and_status
            for ori_neighbor in ori_node.neighbors:
                node_and_status = label_to_node_and_status.get(ori_neighbor.label)
                if node_and_status is None:  # Brand new node
                    visit(ori_neighbor)
                else:
                    nnode, nstatus = node_and_status
                    if nnode is node:  # Self link
                        node.neighbors.append(node)
                    elif nstatus == 'v':  # Unfinished node
                        nnode.neighbors.append(node)
                        node.neighbors.append(nnode)
            current_node_and_status[1] = 'f'

        visit(node)
        return label_to_node_and_status[node.label][0]

# An DFS version
class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return

        label_to_node = {}
        def visit(ori_node):
            node = UndirectedGraphNode(ori_node.label)
            label_to_node[node.label] = node
            for ori_neighbor in ori_node.neighbors:
                if ori_neighbor.label not in label_to_node:
                    visit(ori_neighbor)
                node.neighbors.append(label_to_node[ori_neighbor.label])

        visit(node)
        return label_to_node[node.label]

# A bfs version
class Solution(object):
    def cloneGraph(self, node):
        from collections import deque

        if node is None:
            return

        label_to_node = {}
        queue = deque()
        queue.append(node)
        label_to_node[node.label] = UndirectedGraphNode(node.label)
        while queue:
            head = queue.popleft()
            head_new = label_to_node[head.label]
            for neighbor in head.neighbors:
                if neighbor.label not in label_to_node:
                    label_to_node[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                head_new.neighbors.append(label_to_node[neighbor.label])

        return label_to_node[node.label]

# A non-standard bfs version (queue is not used)
class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return

        label_to_node = {}
        lst = []
        lst.append(node)
        label_to_node[node.label] = UndirectedGraphNode(node.label)
        while lst:
            head = lst.pop()
            head_new = label_to_node[head.label]
            for neighbor in head.neighbors:
                if neighbor.label not in label_to_node:
                    label_to_node[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    lst.append(neighbor)
                head_new.neighbors.append(label_to_node[neighbor.label])

        return label_to_node[node.label]


class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

if __name__ == "__main__":
    n0 = UndirectedGraphNode('0')
    n1 = UndirectedGraphNode('1')
    n2 = UndirectedGraphNode('2')
    n0.neighbors.append(n0)
    n0.neighbors.append(n1)
    n1.neighbors.append(n0)
    n0.neighbors.append(n2)
    n2.neighbors.append(n0)

    Solution().cloneGraph(n0)
