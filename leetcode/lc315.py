# O(n log n) solution using balance binary search tree.
class Solution(object):
    class Tree(object):
        class Node(object):
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None
                self.count = 0
                self.left_and_self_count = 0


        def __init__(self, nums):
            def build_tree(li, ri):
                if li > ri:
                    return None
                mi = (li + ri) // 2
                node = self.Node(sorted_nums[mi])
                node.left = build_tree(li, mi - 1)
                node.right = build_tree(mi + 1, ri)
                return node


            sorted_nums = sorted(nums)
            self.root = build_tree(0, len(sorted_nums) - 1)


        def add(self, val):
            node = self.root
            while True:
                if node.val < val:
                    node = node.right
                else:
                    node.left_and_self_count += 1
                    if node.val == val:
                        node.count += 1
                        break
                    node = node.left


        def count_smaller(self, val):
            count = 0
            node = self.root
            while node.val != val:
                if node.val < val:
                    count += node.left_and_self_count
                    node = node.right
                else:
                    node = node.left
            count += node.left_and_self_count - node.count

            return count


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        
        tree = self.Tree(nums)
        rv = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            x = nums[i]
            rv[i] = tree.count_smaller(x)
            tree.add(x)

        return rv


# Another O(n log n) using Binary Indexed Tree.
class BITSolution(object):
    class BIT(object):
        def __init__(self, nums):
            sorted_nums = sorted(nums)
            self.nums_map = {}
            for i, x in enumerate(sorted_nums, 1):
                self.nums_map[x] = i
            self.tree = [0] * (len(nums) + 1)


        def add(self, val):
            index = self.nums_map[val]
            while index < len(self.tree):
                self.tree[index] += 1
                index += (index & -index)


        def count_smaller(self, val):
            # ``-1`` is appended because we need to count "smaller" instead of
            # "smaller or equal"
            index = self.nums_map[val] - 1
            count = 0
            while index > 0:
                count += self.tree[index]
                index &= ~(index & -index)

            return count


    def countSmaller(self, nums):
        tree = self.BIT(nums)
        rv = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            rv[i] = tree.count_smaller(x)
            tree.add(x)

        return rv



def test():
    for S in (Solution, BITSolution):
        assert S().countSmaller([5,2,6,1]) == [2,1,1,0]
        assert S().countSmaller([5,2,2,6,1]) == [3,1,1,1,0]
        assert S().countSmaller([]) == []
        assert S().countSmaller([1]) == [0]
