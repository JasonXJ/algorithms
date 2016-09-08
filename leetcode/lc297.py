# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        components = []

        def dfs(node):
            if node is None:
                components.append('')
            else:
                components.append(str(node.val))
                dfs(node.left)
                dfs(node.right)


        dfs(root)
        return ','.join(components) + ','
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == ',':
            return None
        self.index = 0

        def dfs():
            if data[self.index] == ',':
                self.index += 1
                return None
            # Otherwise, read an integer
            start = self.index
            if data[self.index] == '-':
                self.index += 1
            while data[self.index] != ',':
                self.index += 1
            node = TreeNode(int(data[start:self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()

            return node


        return dfs()
        

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def test():
    root = TreeNode(1)
    codec = Codec()
    string = codec.serialize(root)
    assert string == '1,,,'
    decoded_tree = codec.deserialize(string)
    assert decoded_tree.val == 1 and decoded_tree.left is None and decoded_tree.right is None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
