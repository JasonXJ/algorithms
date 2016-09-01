from binarytree import BinaryTreeNode

def find_paths(tree, required_sum):
    # The complexity should be O(n*log(n)). We can calculate it as follows:
    #
    # Consider a path from root to some node "nx": r -> n1 -> n2 -> nx. "nx" is
    # invoked in the process 4 times: 1. r -> n1 -> n2 are considered as a
    # prefix of the target path; 2. n1 -> n2 are considered as the prefix; 3.
    # n2 are considered as the prefix 4. neither r, n1 or n2 is part of the
    # prefix.
    #
    # So, for a node "nx", the time it is invoked is its height plus 1. So the
    # over all complexity is O(n log(n))

    results = []

    def recursive(tree, remain_sum, path=tuple()):
        """ Designed to allow nodes' data being zero or negative. ``path`` is
        the required prefix path. ``path == tuple()`` means no prefix path is
        required. """
        if tree is None:
            return

        new_path = path + (tree,)

        if remain_sum == tree.data:
            results.append(new_path)

        if len(path) == 0:
            # Find paths that do not contain node `tree`. Note we only find
            # such paths if ``len(path) == 0``
            recursive(tree.left_child, required_sum)
            recursive(tree.right_child, required_sum)
        recursive(tree.left_child, remain_sum - tree.data, new_path)
        recursive(tree.right_child, remain_sum - tree.data, new_path)

    recursive(tree, required_sum)

    return results

def test_1():
    Node = BinaryTreeNode
    tree = Node((1, 'a'),
                Node((2, 'b'), Node((3, 'c'), Node((0, 'd'), Node((-1, 'e'), Node((1, 'f')))))),
                Node((2, 'g'),
                     Node((3, 'h')),
                     Node((2, 'i'), None, Node((5, 'j'), None, Node((-2, 'k'))))))
    for node in tree.inorder():
        node.data, node._test_1_id= node.data

    results = find_paths(tree, 5)

    results_in_ids = [tuple(node._test_1_id for node in path) for path in results]
    assert len(results_in_ids) == len(set(results_in_ids))
    assert set(results_in_ids) == set([
        ('b', 'c'),
        ('b', 'c', 'd'),
        ('b', 'c', 'd', 'e', 'f'),
        ('a', 'b', 'c', 'd', 'e'),
        ('a', 'g', 'i'),
        ('g', 'h'),
        ('j', ),
        ('i', 'j', 'k'),
    ])
