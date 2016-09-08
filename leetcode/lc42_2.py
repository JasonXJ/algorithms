class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        left_cursor = 0
        left_highest = height[0]
        right_cursor = len(height) - 1
        right_highest = height[len(height) - 1]
        
        rv = 0
        while left_cursor + 1 < right_cursor:
            if left_highest <= right_highest:
                left_cursor += 1
                if left_highest <= height[left_cursor]:
                    # Can trap no water. All water will leak from the left side.
                    left_highest = height[left_cursor]
                else:
                    # Can trap exactly ``left_highest - height[left_cursor]``
                    # water on this location.
                    rv += left_highest - height[left_cursor]
            else:
                # The same as the last "then" clause except replace the "left"s
                # with "right"s and "+=" with "-="
                right_cursor -= 1
                if right_highest <= height[right_cursor]:
                    right_highest = height[right_cursor]
                else:
                    rv += right_highest - height[right_cursor]

        return rv
