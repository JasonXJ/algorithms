from binarytree import BinaryTreeNode
import math

""" 
We use a solution different from in-order traversal here. Note that if we use
in-order traversal, nodes with same values cannot be handled easily.
"""

def is_binary_search_tree(tree):
    def recursive(tree, lower_bound, upper_bound):
        if tree is None:
            return True
        data = tree.data
        # Note that we do not allow duplicated data, so we use "<" instead of
        # "<="
        if (lower_bound < data < upper_bound and
                recursive(tree.left_child, lower_bound, data) and
                recursive(tree.right_child, data, upper_bound)):
            return True
        return False

    return recursive(tree, float('-inf'), float('+inf'))

def test_1():
    # True case
    tree1 = BinaryTreeNode(5,
                           BinaryTreeNode(3, BinaryTreeNode(2), BinaryTreeNode(4)),
                           BinaryTreeNode(7, BinaryTreeNode(6), BinaryTreeNode(8)))
    assert is_binary_search_tree(tree1) == True

    # False case2
    tree2 = BinaryTreeNode(5,
                           BinaryTreeNode(3, BinaryTreeNode(2), BinaryTreeNode(3)),
                           BinaryTreeNode(7, BinaryTreeNode(6), BinaryTreeNode(8)))
    assert is_binary_search_tree(tree2) == False

    # False case3
    tree3 = BinaryTreeNode(5,
                           BinaryTreeNode(3, BinaryTreeNode(2), BinaryTreeNode(3)),
                           BinaryTreeNode(7, BinaryTreeNode(5), BinaryTreeNode(8)))
    assert is_binary_search_tree(tree3) == False
