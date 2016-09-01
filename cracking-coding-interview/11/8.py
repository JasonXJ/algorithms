class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.subtree_size = 1
            self.left = None
            self.right = None
            self.parent = None
        

    def __init__(self):
        self.root = None

    @staticmethod
    def _traceback_increase(start_node):
        current_node = start_node
        current_node.subtree_size += 1
        while current_node.parent is not None:
            current_node = current_node.parent
            current_node.subtree_size += 1


    def insert(self, value):
        new_node = self.Node(value)
        if self.root is None:
            self.root = new_node
        else:
            new_node_parent = self.root
            while True:
                if value == new_node_parent.value:
                    break
                elif value < new_node_parent.value:
                    if new_node_parent.left is None:
                        new_node_parent.left = new_node
                        break
                    else:
                        new_node_parent = new_node_parent.left
                else:
                    if new_node_parent.right is None:
                        new_node_parent.right = new_node
                        break
                    else:
                        new_node_parent = new_node_parent.right

            # All 3 cases need to increase the ``subtree_size``
            self._traceback_increase(new_node_parent)

            # In the case of ``value == new_node_parent.value``, we do not add
            # ``new_node`` into the tree. So this statement has no actual
            # effect in that case.
            new_node.parent = new_node_parent


class Tracker:
    def __init__(self):
        self.tree = BinarySearchTree()

    def track(self, x):
        self.tree.insert(x)

    def getRankOfNumber(self, x):
        rank = 0
        node = self.tree.root
        while node is not None:
            if node.value > x:
                # Search the left subtree
                node = node.left
            else: # node.value <= x
                # Add the whole subtree size of `node` except the part for its
                # right subtree to `rank`
                rank += node.subtree_size
                if node.right is not None:
                    rank -= node.right.subtree_size
                if node.value == x:
                    break  # No next node
                else:  # node.value < x
                    # Still need to search the right subtree
                    node = node.right

        return rank


def test_tracker():
    inputs = [10, 5, 7, 2, 2, 6, 20, 15, 30]
    tracker = Tracker()
    for x in inputs:
        tracker.track(x)
    assert tracker.getRankOfNumber(2) == 2
    assert tracker.getRankOfNumber(5) == 3
    assert tracker.getRankOfNumber(6) == 4
    assert tracker.getRankOfNumber(10) == 6
    assert tracker.getRankOfNumber(15) == 7
    assert tracker.getRankOfNumber(17) == 7
    assert tracker.getRankOfNumber(20) == 8
    assert tracker.getRankOfNumber(25) == 8
    assert tracker.getRankOfNumber(30) == 9
