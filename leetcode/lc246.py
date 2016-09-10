class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pairs = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        l = 0
        r = len(num) - 1
        while l <= r:
            try:
                if pairs[num[l]] != num[r]:
                    return False
            except KeyError:
                return False
            l += 1
            r -= 1
        return True
