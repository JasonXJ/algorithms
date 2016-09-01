class Solution(object):
    def mySqrt(self, x):
        l = 0
        h = x
        while l <= h:
            mid = (l + h) // 2
            power = mid*mid
            if power == x:
                return mid
            elif power > x:
                h = mid - 1
            else:
                l = mid + 1
        return h
