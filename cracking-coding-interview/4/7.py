from binarytree import BinaryTreeNode

def common_ancestor(tree, node1, node2):
    class _CommonAncestorFound(Exception):
        def __init__(self, node):
            self.node = node
    
    def recursive(tree):
        """ If `tree` is the common ancestor, `_CommonAncestorFound(tree)` is
        raised. If `node1`/`node2` is in this subtree, return True, otherwise
        return False.  """
        if tree == None:
            return False
        if tree == node1 or tree == node2:
            # Only need to find another node in the left or right subtree.
            if recursive(tree.left_child) or recursive(tree.right_child):
                raise _CommonAncestorFound(tree)
            return True
        else:
            l_found = recursive(tree.left_child)
            r_found = recursive(tree.right_child)
            if l_found and r_found:
                raise _CommonAncestorFound(tree)
            elif l_found or r_found:
                return True
            return False

    try:
        recursive(tree)
    except _CommonAncestorFound as e:
        return e.node
    else:
        assert False, "No common ancestor found, the tree may be corrupt."

def test_1():
    Node = BinaryTreeNode
    tree = Node(1,
                Node(2,
                     Node(4),
                     Node(5)),
                Node(3,
                     Node(6),
                     Node(7)))

    nodes = {node.data:node for node in tree.inorder()}
    
    assert common_ancestor(tree, nodes[4], nodes[5]).data == 2
    assert common_ancestor(tree, nodes[4], nodes[6]).data == 1
    assert common_ancestor(tree, nodes[1], nodes[6]).data == 1
    assert common_ancestor(tree, nodes[6], nodes[1]).data == 1
