class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) <= 1:
            return True
        x_min = min(points)[0]
        x_max = max(points)[0]
        double_x_mid = x_min + x_max
        point_set = set(tuple(p) for p in points)
        for x, y in points:
            if (double_x_mid - x, y) not in point_set:
                return False
        return True
