from binarytree import BinaryTreeNode

def is_balanced(tree_node):
    return find_unbalance_subtree(tree_node) is None

def find_unbalance_subtree(tree_node):
    class NonBalance(Exception):
        def __init__(self, node):
            self.node = node

    def recursive(tree_node):
        """ Return height of the subtree rooted at `tree_node` if the subtree
        is balanced. Otherwise raise `NonBalance(tree_node)` """
        if tree_node is None:
            # Tree with only root node has a height of 1, so tree with no node
            # has a height of -1
            return -1
        height1 = recursive(tree_node.left_child)
        height2 = recursive(tree_node.right_child)
        if height1 < height2:
            height1, height2 = height2, height1
        if height1 - height2 > 1:
            raise NonBalance(tree_node)
        return height1 + 1

    try:
        recursive(tree_node)
    except NonBalance as e:
        return e.node

    return None

def test_find_unbalance_subtree():
    # Balanced case
    tree1 = BinaryTreeNode(1,
                   BinaryTreeNode(2,
                                  BinaryTreeNode(4),
                                  BinaryTreeNode(5)),
                   BinaryTreeNode(3))
    assert find_unbalance_subtree(tree1) is None

    # Root node unbalanced
    tree2 = BinaryTreeNode(1,
                   BinaryTreeNode(2,
                                  BinaryTreeNode(4),
                                  BinaryTreeNode(5, BinaryTreeNode(6), None)),
                   BinaryTreeNode(3))
    assert find_unbalance_subtree(tree2).data == 1

    # Subnode 5 is unbalanced.
    tree3 = BinaryTreeNode(1,
                   BinaryTreeNode(2,
                                  BinaryTreeNode(4),
                                  BinaryTreeNode(5, BinaryTreeNode(6, BinaryTreeNode(7)), None)),
                   BinaryTreeNode(3))
    assert find_unbalance_subtree(tree3).data == 5
