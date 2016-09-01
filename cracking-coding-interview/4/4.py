from binarytree import BinaryTreeNode

def nodes_in_levels(tree):
    """ Gather node of a tree level by level """
    nodes = []

    def visit(node, depth):
        if node is None:
            return

        if depth + 1 > len(nodes):
            nodes.append([node])
        else:
            nodes[depth].append(node)
        
        visit(node.left_child, depth+1)
        visit(node.right_child, depth+1)

    visit(tree, 0)

    return nodes

def test_1():
    root = BinaryTreeNode(1,
                   BinaryTreeNode(2,
                                  BinaryTreeNode(4, BinaryTreeNode(8)),
                                  BinaryTreeNode(5)),
                   BinaryTreeNode(3,
                                  BinaryTreeNode(6),
                                  BinaryTreeNode(7, None, BinaryTreeNode(9))))
    assert ([[node.data for node in level] for level in nodes_in_levels(root)] ==
            [[1], [2, 3], [4,5,6,7], [8,9]])
