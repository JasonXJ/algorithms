class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        assert len(digits) > 0
        rrv = []
        carry = 1
        i = len(digits) - 1
        while True:
            if i >= 0:
                x = digits[i]
                i -= 1
            else:
                x = 0
                if carry == 0:
                    break
            x += carry
            if x >= 10:
                carry = 1
                x -= 10
            else:
                carry = 0
            rrv.append(x)

        return list(reversed(rrv))


def test():
    assert Solution().plusOne([0]) == [1]
    assert Solution().plusOne([1,0]) == [1,1]
    assert Solution().plusOne([1,9]) == [2,0]
    assert Solution().plusOne([9,9,9]) == [1,0,0,0]
