class Solution(object):
    @staticmethod
    def reverse_longest_ascending_sequence(nums):
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        return i

    @staticmethod
    def reverse(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def nextPermutation(self, nums):
        if len(nums) <= 1:
            return
        seq_left = self.reverse_longest_ascending_sequence(nums)
        self.reverse(nums, seq_left, len(nums)-1)
        if seq_left == 0:
            return

        to_promote = nums[seq_left-1]
        # nums[seq_left:] now is sorted ascendingly
        i = seq_left
        while nums[i] <= to_promote:
            i += 1
        
        nums[seq_left-1], nums[i] = nums[i], nums[seq_left-1]

        # Make sure nums[seq_left:] is sorted
        i1 = i + 1
        while i1 < len(nums) and nums[i1-1] > nums[i1]:
            nums[i1-1], nums[i1] = nums[i1], nums[i1-1]
        i2 = i - 1
        while i2 >= seq_left and nums[i2] > nums[i2+1]:
            nums[i2], nums[i2+1] = nums[i2+1], nums[i2]

def test():
    f = Solution().nextPermutation
    def subtest(lst, *args):
        for x in args:
            f(lst)
            assert lst == x
    subtest([1], [1])
    subtest([1, 2], [2, 1], [1, 2])
    subtest([1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1], [1, 2, 3])
    subtest([1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 1, 2])
