RED = 0
BLACK = 1

class RBNode:
    """ A node in a red black tree. Note that the instance of this class only
    store the data and has no other functionality, so, for example, setting
    ``n.left`` will not automatically update ``n.left_subtree_size``. """
    # TODO: Maybe we can set the `__slot__`
    def __init__(self, value, count, color, left, right, parent, left_subtree_size,
                 right_subtree_size):
        if color not in (RED, BLACK):
            raise ValueError
        self.value = value
        self.count = count
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent
        self.left_subtree_size = left_subtree_size
        self.right_subtree_size = right_subtree_size


class RBTree:
    """ Red black tree with subtree size information stored in nodes.
    
    This implementation is based on Red Black Tree section in "Introduction to
    Algorithm". Also note that the subtree sizes (attributes
    `left_subtree_size` and `right_subtree_size`) of each node take the `count`
    of subtrees' nodes into account.
    """

    def __init__(self):
        self._NIL_NODE = RBNode(None, None, BLACK, None, None, None, None, None)
        self.root = self._NIL_NODE


    # O(log n)
    def insert(self, value):
        parent = self._NIL_NODE
        cursor = self.root
        while cursor is not self._NIL_NODE and cursor.value != value:
            parent = cursor
            if value < cursor.value:
                cursor.left_subtree_size += 1
                cursor = cursor.left
            else:
                cursor.right_subtree_size += 1
                cursor = cursor.right

        if cursor is not self._NIL_NODE:  # The node alread exists
            cursor.count += 1
        else:
            new_node = RBNode(value, 1, RED, self._NIL_NODE, self._NIL_NODE, parent, 0, 0)
            if parent is self._NIL_NODE:  # Empty tree
                self.root = new_node
                new_node.color = BLACK
            else:
                if value < parent.value:
                    parent.left = new_node
                else:
                    parent.right = new_node
                self._fix_insert(new_node)


    # O(log n)
    def delete(self, value):
        raise NotImplementedError


    # O(log n)
    def count(self, value):
        return self.count_equal_and_count_less(value)[0]
    

    # O(log n)
    def count_less(self, value):
        return self.count_equal_and_count_less(value)[1]


    # O(log n)
    def count_less_and_equal(self, value):
        return sum(self.count_equal_and_count_less(value))

    
    # O(log n)
    def count_equal_and_count_less(self, value):
        """ Return ``(n_equal, n_less)``, where `n_equal` is the number of
        `value` inserted and `n_less` is the number of values < `value`
        inserted.  """
        n_less = 0
        cursor = self.root
        while cursor is not self._NIL_NODE:
            if cursor.value == value:
                n_less += cursor.left_subtree_size
                return cursor.count, n_less
            elif cursor.value < value:
                n_less += cursor.left_subtree_size + cursor.count
                cursor = cursor.right
            else:
                cursor = cursor.left

        return 0, n_less


    def total_size(self, node=None):
        if node is None:
            node = self.root
        if node is self._NIL_NODE:
            raise ValueError
        return node.left_subtree_size + node.right_subtree_size + node.count
    

    def _left_rotation(self, node):
        """ Note that this function assumes that ``node.right`` is a normal
        node. Subtree size is properly handled. """
        # First update the subtree sizes
        node.right_subtree_size = node.right.left_subtree_size
        node.right.left_subtree_size = self.total_size(node)

        # Update the links
        new_subtree_root = node.right
        node.right = new_subtree_root.left
        # Note that the next statement is OK even if ``node.right is
        # self._NIL_NODE``
        node.right.parent = node
        new_subtree_root.parent = node.parent
        node.parent = new_subtree_root
        new_subtree_root.left = node
        if new_subtree_root.parent is not self._NIL_NODE:
            if new_subtree_root.parent.left is node:
                new_subtree_root.parent.left = new_subtree_root
            else:
                new_subtree_root.parent.right = new_subtree_root
        else:  # `node` is the original root
            self.root = new_subtree_root


    def _right_rotation(self, node):
        """ Note that this function assumes that ``node.left`` is a normal
        node. Subtree size is properly handled. """
        # First update the subtree sizes
        node.left_subtree_size = node.left.right_subtree_size
        node.left.right_subtree_size = self.total_size(node)

        # Update the links
        new_subtree_root = node.left
        node.left = new_subtree_root.right
        node.left.parent = node
        new_subtree_root.parent = node.parent
        node.parent = new_subtree_root
        new_subtree_root.right = node
        if new_subtree_root.parent is not self._NIL_NODE:
            if new_subtree_root.parent.left is node:
                new_subtree_root.parent.left = new_subtree_root
            else:
                new_subtree_root.parent.right = new_subtree_root
        else:
            self.root = new_subtree_root
        

    def _fix_insert(self, node):
        while node.parent.color == RED:
            if node.parent is node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    # Note that `uncle` is definitely not ``self._NIL_NODE``.
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:  # ``uncle.color == BLACK``
                    if node is node.parent.right:
                        # Need to rotate it first.
                        node = node.parent
                        self._left_rotation(node)
                        # Fall through
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._right_rotation(node.parent.parent)
                    # Note that after the rotation, ``node.parent`` is not
                    # changed, so its color is still black and the while loop
                    # will not enter next iteration.
            else:  # ``node.parent is node.parent.parent.right``
                # This is basically the same as the "then" clause above except
                # "left"s and "right"s are swapped.
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self._right_rotation(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._left_rotation(node.parent.parent)

        self.root.color = BLACK


    def inorder_traversal(self):
        stack = []
        def expand_node(node):
            while node is not self._NIL_NODE:
                stack.append(node)
                node = node.left


        expand_node(self.root)
        while stack:
            node = stack.pop()
            yield (node.value, node.count)
            expand_node(node.right)


    def _integrity_test(self, inserted_values):
        """ Raise :exc:`AssertionError` if the RBTree has any problems. """
        # BST property test
        from collections import Counter
        assert list(self.inorder_traversal()) == sorted(Counter(inserted_values).items())


        # RBTree property test
        def test_rbtree_property(node, must_be_black):
            # Property 1: Every node is either red or black.
            assert node.color in (BLACK, RED)

            # Property 3: Every leaf ( NIL ) is black.
            if node is self._NIL_NODE:
                assert node.color == BLACK
                return 1

            # Property 2: The root is black; and
            # Property 4: If a node is red, then both its children are black.
            if must_be_black:
                assert node.color == BLACK
            children_must_be_black = node.color == RED

            # Property 5: For each node, all simple paths from the node to
            # descendant leaves contain the same number of black nodes.
            black_height1 = test_rbtree_property(node.left, children_must_be_black)
            black_height2 = test_rbtree_property(node.right, children_must_be_black)
            assert black_height1 == black_height2

            new_black_height = black_height1
            if node.color == BLACK:
                new_black_height += 1
            return new_black_height


        test_rbtree_property(self.root, True)


            
        # Subtree sizes test
        def test_subtree_sizes(node):
            if node is self._NIL_NODE:
                return 0
            left_subtree_size = test_subtree_sizes(node.left)
            right_subtree_size = test_subtree_sizes(node.right)
            assert left_subtree_size == node.left_subtree_size
            assert right_subtree_size == node.right_subtree_size

            return left_subtree_size + right_subtree_size + node.count


        test_subtree_sizes(self.root)

        
        
def test_RBTree():
    # XXX Note that deletion is not tested.
    from collections import Counter

    def _test(values):
        tree = RBTree()
        tree._integrity_test([])
        for x in values:
            tree.insert(x)
        tree._integrity_test(values)

        if len(values) == 0:
            assert (tree.count(10) == tree.count_less(10) ==
                    tree.count_less_and_equal(10) == 0)
        else:
            # Test the count methods
            values_and_counts = sorted(Counter(values).items())
            cumulated_counts = [0]
            for value, count in values_and_counts:
                cumulated_counts.append(cumulated_counts[-1] + count)
            for i, (value, count) in enumerate(values_and_counts):
                assert tree.count(value) == count
                assert tree.count_less(value) == cumulated_counts[i]
                assert tree.count_less_and_equal(value) == cumulated_counts[i+1]

            # Test the count methods for values which is not inserted
            nonexistent_values = [values_and_counts[0][0] - 1]
            for i in range(len(values_and_counts) - 1):
                # The mean of two adjacent values should be nonexistent unless
                # I am very unlucky and overflow `float`
                nonexistent_values.append(
                    (values_and_counts[i][0] + values_and_counts[i+1][0]) / 2
                )
            nonexistent_values.append(values_and_counts[-1][0] + 1)
            assert len(nonexistent_values) == len(cumulated_counts)
            for value, ccount in zip(nonexistent_values, cumulated_counts):
                assert tree.count(value) == 0
                assert (tree.count_less(value) ==
                        tree.count_less_and_equal(value) == ccount)

        return tree
        

    tree = _test([1, 1, 2])
    assert tree.count(0) == 0
    assert tree.count(100) == 0
    assert tree.count_less(100) == 3

    # No/Single node
    _test([])
    _test([1])

    # Sorted values
    _test(list(range(2)))
    _test(list(range(10)))
    _test(list(range(-1000, 1000)))

    # Reverse sorted values
    _test(list(range(1000, -1000, -1)))

    # Random values
    import random
    for _ in range(10):
        _test([random.random() for _ in range(10000)])

    # Integer random values (many duplications)
    import random
    for _ in range(10):
        _test([random.randint(1, 100) for _ in range(10000)])
