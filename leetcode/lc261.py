from collections import namedtuple

Union = namedtuple('Union', 'parent, size')

class Solution(object):
    class UnionFind(object):
        def __init__(self, n):
            self.unions = [Union(i, 1) for i in range(n)]
        

        def link(self, i, j):
            uid1 = self.union_id(i)
            uid2 = self.union_id(j)
            if uid1 == uid2:
                return False
            if self.unions[uid1].size > self.unions[uid2].size:
                uid1, uid2 = uid2, uid1
            self.unions[uid1] = self.unions[uid1]._replace(parent=uid2)
            self.unions[uid2] = self.unions[uid2]._replace(
                size=self.unions[uid2].size + self.unions[uid1].size
            )
            return True
                
            
        def union_id(self, i):
            while self.unions[i].parent != i:
                i = self.unions[i].parent
            return i

        

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        uf = self.UnionFind(n)
        for i, j in edges:
            if uf.link(i, j) == False:
                return False

        return True
