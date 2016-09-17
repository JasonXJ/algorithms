# NOTE: There are some posts about using binary search, which is interesting
# because it could be faster when the black area is close to the area of the
# whole rectangle.
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if len(image) == 0 or len(image[0]) == 0:
            return 0
        x_max = len(image)
        y_max = len(image[0])
        rectangle = [x, y, x, y]
        discovered = set()
        
        def dfs(x, y):
            discovered.add((x,y))
            if x < rectangle[0]:
                rectangle[0] = x
            elif x > rectangle[2]:
                rectangle[2] = x
            if y < rectangle[1]:
                rectangle[1] = y
            elif y > rectangle[3]:
                rectangle[3] = y
            for x1, y1 in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if (0 <= x1 < x_max and 0 <= y1 < y_max and
                        image[x1][y1] == '1' and (x1, y1) not in discovered):
                    dfs(x1, y1)


        dfs(x, y)
        return (rectangle[2] - rectangle[0] + 1) * (rectangle[3] - rectangle[1] + 1)


def test():
    assert Solution().minArea(["0010","0110","0100"], 0, 2) == 6
