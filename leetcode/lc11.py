""" This is a O(n log n) solution """

class Solution(object):
    def maxArea(self, height):
        valid = [True] * len(height)
        left_most_available = 0
        right_most_available = len(height) - 1
        sorted_height_index = sorted((height[i], i) for i in range(len(height)))
        # Note that we delete the highest one because when we process it, there
        # is no item left to pair with it.
        del sorted_height_index[-1]

        max_area = 0
        for height, index in sorted_height_index:
            valid[index] = False

            # Update `left_most_available` and `right_most_available` (We don't
            # need to worry about out-of-range because there will always be at
            # least one element (the one with maximum height) in `valid` that
            # is True.
            while not valid[left_most_available]:
                left_most_available += 1
            while not valid[right_most_available]:
                right_most_available -= 1

            area = max(abs(index-left_most_available), abs(index-right_most_available)) * height
            if area > max_area:
                max_area = area

        return max_area
