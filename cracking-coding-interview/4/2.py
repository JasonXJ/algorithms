import graph

def route_exist(node1, node2, method=graph.dfs):
    for node in method(node1):
        if node == node2:
            return True

    return False

def test_route_exist():
    def _route_exist(node1, node2):
        r1 = route_exist(node1, node2, method=graph.dfs)
        r2 = route_exist(node1, node2, method=graph.bfs)
        assert r1 == r2
        return r1

    nodes = graph.get_example_graph()

    assert _route_exist(nodes[0], nodes[4]) == True
    assert _route_exist(nodes[4], nodes[0]) == False
    assert _route_exist(nodes[4], nodes[2]) == True
    assert _route_exist(nodes[1], nodes[3]) == True
