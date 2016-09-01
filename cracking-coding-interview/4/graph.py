from collections import deque

class DirectedGraphNode:
    def __init__(self, data, adjacent_nodes=tuple()):
        self.data = data
        self.adjacent_nodes = adjacent_nodes

def dfs(start_node):
    visited_nodes = set()

    def recursive(current_node):
        for node in current_node.adjacent_nodes:
            if node not in visited_nodes:
                visited_nodes.add(node)
                yield node
                yield from recursive(node)

    visited_nodes.add(start_node)
    yield start_node
    yield from recursive(start_node)

def bfs(start_node):
    visited_nodes = set()
    queue = deque()

    def visit(node):
        visited_nodes.add(node)
        queue.append(node)
        yield node

    yield from visit(start_node)
    while len(queue) != 0:
        current_node = queue.popleft()
        for node in current_node.adjacent_nodes:
            if node not in visited_nodes:
                yield from visit(node)

def get_example_graph():
    nodes = [
        DirectedGraphNode(0),
        DirectedGraphNode(1),
        DirectedGraphNode(2),
        DirectedGraphNode(3),
        DirectedGraphNode(4),
    ]

    nodes[0].adjacent_nodes = (nodes[1],)
    nodes[1].adjacent_nodes = (nodes[2], nodes[3])
    nodes[2].adjacent_nodes = (nodes[4],)
    nodes[3].adjacent_nodes = (nodes[0], nodes[2])
    nodes[4].adjacent_nodes = (nodes[2],)

    return nodes

def test_DirectedGraphNode():
    nodes = get_example_graph()

    assert [node.data for node in dfs(nodes[0])] == [0, 1, 2, 4, 3]
    assert [node.data for node in bfs(nodes[0])] == [0, 1, 2, 3, 4]
