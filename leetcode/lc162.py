class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NINF = float('-inf')
        def safe_get(index):
            if 0 <= index < len(nums):
                return nums[index]
            return NINF

        l = 0
        r = len(nums) - 1
        while True:
            m = (l + r) // 2
            v_m = nums[m]
            v_m_l = safe_get(m-1)
            v_m_r = safe_get(m+1)
            if v_m > v_m_l and v_m > v_m_r:
                return m
            elif v_m < v_m_l:
                r = m - 1
            else:  # v_m < v_m_r
                l = m + 1


def test():
    assert Solution().findPeakElement([1,2,3,1]) == 2
    assert Solution().findPeakElement([1,2,3,4,5,6]) == 5
    assert Solution().findPeakElement([4,3,2,1]) == 0
    assert Solution().findPeakElement([1,2,5,2,1]) == 2
    assert Solution().findPeakElement([1,2,1,2,1]) in (1, 4)
    
