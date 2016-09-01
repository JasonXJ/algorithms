class Solution(object):
    def largestRectangleArea(self, height):
        # An O(n) algorithm. (Each element is pushed and popped into/from the
        # stack at most once.)

        # Add a sentinel to help with cleaning the stack.
        height_with_sentinel = height[:] + [0]
        max_area = 0

        # Rectangles are pushed into the stack in height-ascending order. If a
        # new rectangle is shorter than previous, it is merged with previous
        # rectangle(s) until the merged rectangle is the highest. The stack is
        # initialized with a sentinel element of negative height.
        stack = [(-1, 0, 0)]  # Element: (height, left boundary, right boundary)

        for i in range(len(height_with_sentinel)):
            h = height_with_sentinel[i]
            if h > stack[-1][0]:
                stack.append((h, i, i+1))
            else:  # h <= ... . Let's merge.
                right_boundary = stack[-1][2]
                # Pop elements and check if they can form a large enough area.
                while True:
                    top = stack.pop()
                    # height*(right_boundary-left_boundary)
                    area = top[0] * (right_boundary - top[1])
                    if area > max_area:
                        max_area = area
                    if stack[-1][0] < h:
                        break
                # Push the merged rectangle
                stack.append((h, top[1], i+1))

        return max_area

def test():
    f = Solution().largestRectangleArea
    assert f([2,1,5,6,2,3]) == 10
    assert f([2,1,5,6,5,2,3]) == 15
    assert f([2,1,5,6,4,2,3]) == 12
    assert f([2,1,5,6,4,2,3,5,6,7]) == 16
    assert f([2,1,5,6,4,2,3,6,6,7]) == 18
    assert f([]) == 0
    assert f([2]) == 2
