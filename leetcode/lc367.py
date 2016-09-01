# A binary search solution

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        root = 1
        while root*root < num:
            root *= 2
        if root*root == num:
            return True

        upper = root - 1
        lower = root // 2 + 1
        while lower <= upper:
            mid = (lower + upper) // 2
            mid_square = mid*mid
            if mid_square == num:
                return True
            elif mid_square < num:
                lower = mid + 1
            else:
                upper = mid - 1

        return False

if __name__ == "__main__":
    assert Solution().isPerfectSquare(1)
    assert Solution().isPerfectSquare(4)
    assert Solution().isPerfectSquare(9)
    assert Solution().isPerfectSquare(16)

    for x in range(1, 15):
        if x not in (1, 4, 9):
            assert not Solution().isPerfectSquare(x)
