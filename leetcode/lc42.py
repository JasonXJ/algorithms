class Solution(object):
    def trap(self, height):
        if len(height) == 0:
            return 0

        water = 0
        left_index = 0
        right_index = len(height) - 1
        left_water_level = 0
        right_water_level = 0
        
        while right_index >= left_index:
            left_height = height[left_index]
            right_height = height[right_index]
            if left_height <= right_height:
                # We can safely increase the left water level
                if left_height > left_water_level:
                    left_water_level = left_height
                else:
                    water += left_water_level - left_height
                left_index += 1
            else:
                # We can safely increase the right water level
                if right_height > right_water_level:
                    right_water_level = right_height
                else:
                    water += right_water_level - right_height
                right_index -= 1

        return water

def test():
    f = Solution().trap
    assert f([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
