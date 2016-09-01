from rbtree import RBTree

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if len(nums) == 0 or lower > upper:
            return 0

        cumulated_nums = [nums[0]]
        for x in nums[1:]:
            cumulated_nums.append(cumulated_nums[-1] + x)

        rbtree = RBTree()
        rbtree.insert(0)
        total_count = 0
        for x in cumulated_nums:
            adjusted_lower = x - upper
            adjusted_upper = x - lower
            total_count += (rbtree.count_less_and_equal(adjusted_upper) -
                            rbtree.count_less(adjusted_lower))
            rbtree.insert(x)

        return total_count


if __name__ == "__main__":
    f = Solution().countRangeSum
    # import ipdb
    # ipdb.set_trace()
    print(f([-2, 5, -3, -1], -2, 2))
    assert f([-2, 5, -1], -2, 2) == 3
    assert f([-2, 5, -3, -1], -2, 2) == 6
