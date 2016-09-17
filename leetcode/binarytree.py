from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def __str__(self):
        return 'TreeNode({!r})'.format(self.val)


    def __repr__(self):
        return self.__str__()
    

def from_list(lst):
    """ Construct and return a tree. We use the leetcode binary tree
    representation here. See https://leetcode.com/faq/#binary-tree """
    if len(lst) == 0 or lst[0] is None:
        return None
    root = TreeNode(lst[0])
    q = deque()
    q.append(root)
    index = 1

    def new_node():
        if index < len(lst) and lst[index] is not None:
            node = TreeNode(lst[index])
            q.append(node)
            return node
        return None


    while index < len(lst):
        left_node = new_node()
        index += 1
        right_node = new_node()
        index += 1
        parent = q.popleft()
        parent.left = left_node
        parent.right = right_node

    return root


def test_from_list():
    assert from_list([]) is None
    assert from_list([None]) is None

    t1 = from_list([1,2,3])
    assert t1.val == 1
    assert (t1.left.val == 2 and t1.left.left is None and t1.left.right is None)
    assert (t1.right.val == 3 and t1.right.left is None and t1.right.right is None)

    t2 = from_list([1, None, 2, 3, None, None, 4])
    assert t2.val == 1 and t2.left is None
    t2n2 = t2.right
    assert t2n2.val == 2 and t2n2.right is None
    t2n3 = t2n2.left
    assert t2n3.val == 3 and t2n3.left is None
    t2n4 = t2n3.right
    assert t2n4.val == 4 and t2n4.left is None and t2n4.right is None
