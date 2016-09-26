class Solution(object):
    """ O(n) time and O(log n) ~ O(n) space solution using inorder traversal.
    The idea is that inorder traversal on a normal BST generates a sorted
    array. Swapping two nodes in the BST could results in the following 3
    situations:

    1. Swapping same values: [1,2,3,3,5] -> [1,2,3,3,5] (3 and 3 are swapped).
       Need to do nothing.
    2. Swapping two "neighbours": [1,2,3,5,6] -> [1,2,5,3,6] (3 and 5 are
       swapped). In the code below, exactly 1 pair of problematic nodes will be
       discovered.  We just need to swap the values in the pair.
    3. Swapping two other nodes: [1,2,3,4,5,6] -> [1,5,3,4,2,6] (2 and 5 are
       swapped). In the code below, exactly 2 pairs of problematic nodes will
       be discovered.  We need to swap the values of the first node of the
       first pair and the second node of the second pair.
    """
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        node_pairs = []
        
        dummy = TreeNode(float('-inf'))
        def inorder(node=root, previous_node=dummy):
            if node.left is not None:
                previous_node = inorder(node.left, previous_node)
            if node.val < previous_node.val:
                node_pairs.append((previous_node, node))
            previous_node = node
            if node.right is not None:
                previous_node = inorder(node.right, previous_node)
            return previous_node
        
        inorder()

        if len(node_pairs) == 0:
            pass
        else:
            assert len(node_pairs) in (1, 2)
            if len(node_pairs) == 1:
                x, y = node_pairs[0]
            else:
                x = node_pairs[0][0]
                y = node_pairs[1][1]
            x.val, y.val = y.val, x.val
