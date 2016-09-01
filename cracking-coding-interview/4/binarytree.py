class BinaryTreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.parent = None

        if self.left_child is not None:
            self.left_child.parent = self
        if self.right_child is not None:
            self.right_child.parent = self

    def __str__(self):
        return "<BinaryTreeNode: data={}>".format(self.data)

    def inorder(self):
        def recursive(node):
            if node is not None:
                yield from recursive(node.left_child)
                yield node
                yield from recursive(node.right_child)

        yield from recursive(self)

def test_btn():
    tree = BinaryTreeNode(3,
                   BinaryTreeNode(1, BinaryTreeNode(0), BinaryTreeNode(2)),
                   BinaryTreeNode(6,
                                  BinaryTreeNode(4, None, BinaryTreeNode(5)),
                                  BinaryTreeNode(7)))
    assert [node.data for node in tree.inorder()] == list(range(8))
