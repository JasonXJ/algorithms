from binarytree import BinaryTreeNode

def get_next_node(node):
    """ Find the next node (in respect of in-order) of `node`  """

    if node.right_child is not None:
        # First case: ``node`` has right child, the next node is in the subtree
        # rooted at the right child, and it is leftmost node in this subtree.
        current_node = node.right_child
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node
    else:
        # Second case: The next node is (grand)parent, which is the first node
        # to the right of `node`
        current_node = node
        while current_node.parent is not None:
            if current_node.parent.left_child == current_node:
                return current_node.parent
            current_node = current_node.parent

def test_1():
    from operator import attrgetter
    tree = BinaryTreeNode(3,
                   BinaryTreeNode(1, BinaryTreeNode(0), BinaryTreeNode(2)),
                   BinaryTreeNode(6,
                                  BinaryTreeNode(4, None, BinaryTreeNode(5)),
                                  BinaryTreeNode(7)))
    nodes = list(tree.inorder())
    assert nodes == sorted(nodes, key=attrgetter('data'))

    expected_next_nodes = nodes[1:] + [None]

    for node, next_node in zip(nodes, expected_next_nodes):
        assert get_next_node(node) is next_node
